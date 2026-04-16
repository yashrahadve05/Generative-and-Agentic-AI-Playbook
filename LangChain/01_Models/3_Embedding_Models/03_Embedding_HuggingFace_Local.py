# 03_Embedding_HuggingFace_Local.py

from unittest import result

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Throttling is a JavaScript technique that controls how often a function executes within a fixed time interval.",
    "It improves performance by ensuring functions run at a consistent rate during frequent events.",
    "Limits function execution to once per specified time frame",
    "Prevents performance issues during heavy events like scrolling or resizing.",
    "Ensures smoother and more efficient event handling."
]


vector = embedding.embed_documents(documents)

result(str(vector))