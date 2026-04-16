# 02_Embedding_OpenAI_Docs.py

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=32
)

documents = [
    "Throttling is a JavaScript technique that controls how often a function executes within a fixed time interval.",
    "It improves performance by ensuring functions run at a consistent rate during frequent events.",
    "Limits function execution to once per specified time frame",
    "Prevents performance issues during heavy events like scrolling or resizing.",
    "Ensures smoother and more efficient event handling."
]

result = embedding.embed_documents(documents)

print(str(result))