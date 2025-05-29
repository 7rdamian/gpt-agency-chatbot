from flask import Flask, request, render_template, jsonify
from app.rag import answer_question
from dotenv import load_dotenv

load_dotenv()

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
    app.run(debug=True)
