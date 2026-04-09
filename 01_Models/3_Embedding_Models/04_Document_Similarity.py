# 04_Document_Similarity.py

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=32
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]


query = "Tell me about Rohit Sharma"

docs_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

score = cosine_similarity([query_embedding], docs_embedding)[0]

index, score = sorted(list(enumerate(score)), key=lambda x:x[1])[-1]


print("Query: ", query)
print("Document Index: ", documents[index])
print("Similarity Score: ", score)