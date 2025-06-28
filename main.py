from flask import Flask, request, render_template, jsonify
from app.rag import answer_question


def load_documents_on_startup():
    from langchain_huggingface import HuggingFaceEmbeddings 
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import Chroma
    import os

    documents_folder = "docs"

    if not os.path.exists(documents_folder):
        print("Documents folder not found!")
        exit()

    all_files = os.listdir(documents_folder)

    txt_files = []
    for file in all_files:
        if file.endswith('.txt'):
            txt_files.append(file)

    if len(txt_files) == 0:
        print("No .txt files found in documents folder")
        exit()

    all_texts = []
    for filename in txt_files:
        file_path = os.path.join(documents_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            all_texts.append(content)

    raw_text = ""
    for text in all_texts:
        raw_text = raw_text + text + "\n\n"

    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=300)
    docs = splitter.create_documents([raw_text])

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(docs, embedding, persist_directory="./db")
    db.persist()

    print("Documents saved")


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    answer = answer_question(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    print("Loading documents on startup...")
    load_documents_on_startup()

    app.run(debug=True)
