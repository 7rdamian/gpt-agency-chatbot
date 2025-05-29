from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Load raw document
with open("user_documents.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Create chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=300)
docs = splitter.create_documents([raw_text])

# Embed and store
embedding = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")
db = Chroma.from_documents(docs, embedding, persist_directory="./db")
db.persist()

print("Documents loaded, chunked, embedded, and saved.")
