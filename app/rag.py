from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_together import Together
from dotenv import load_dotenv
import os

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma(persist_directory="./db", embedding_function=embedding)

retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": 5})

llm = Together(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", 
    temperature=0.7,
    max_tokens=1024,
    together_api_key=os.getenv("TOGETHER_API_KEY")
)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def answer_question(question: str) -> str:
    return qa_chain.invoke({"query": question})["result"]
