# 01_Embedding_OpenAI_Query.py

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=32
)

result = embedding.embed_query("""
Currying is used in JavaScript to break down complex function calls into smaller, more manageable steps. It transforms a function with multiple arguments into a series of functions, each taking a single argument.
It converts a function with multiple parameters into a sequence of functions.
Each function takes a single argument and returns another function until all arguments are received.
Helps in functional programming by enabling function reusability and composition.
""")

print(str(result))