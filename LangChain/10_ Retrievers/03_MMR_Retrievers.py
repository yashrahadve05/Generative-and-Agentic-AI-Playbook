# 03_MMR_Retrievers.py

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings


docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

# Initialize OpenAI embeddings
embedding_model = OpenAIEmbeddings()

# Step 2: Create the FAISS vector store from documents
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

# Enable MMR in the retriever
retriever = vectorstore.as_retriever(
    search_type="mmr", # <-- This enables MMR
    search_kwargs={
        "k": 3, # k = Top results
        "lambda_mult": 0.5 # lambda_mult = relevance-diersity balance
    }
)

query = "What is LangChain"

result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"\n --- Result {i+1} ---")
    print(f"Content: ", doc.page_content)


