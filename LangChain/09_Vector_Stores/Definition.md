## **Vector stores:** This are specialized databases that store embeddings (numeric vectors that capture semantic meaning) and provide fast similarity search. In LangChain, vector stores are the backbone of Retrieval-Augmented Generation (RAG) workflows where we embed our documents, store them in a vector store, then retrieve semantically relevant chunks at query time and feed them to an LLM.

or

## **Vector Stores:** A vector store is a system designed to store and retrieve data represented as numerical vectors.

## Key Featues:
1. **Storage -** Ensures that vectors and their associated metadata are retaiened, whether **in-memory** for quick lookups or **on-disk** for durability and large-scale use.

2. **Similarity Search -** Helps to retrieve the vectors most similar to a quary vector.

3. **Indexing -** Provide a data structure or method that enables fast similarity searches on high-dimensional vector (e.g., approximate newarest neighbor lookups).

4. **CRUD Operations -** Manage the lifecycles of data-adding new vectors, reading them, updating existing entries, removing outdated vectors.


## Use Cases
1. Semantic Search
2. RAG
3. Recommender Systems
4. Image/Multimedia Search

## Key Terms
- **Embedding:** A fixed-length numeric vector representing the semantic content of a text (or image/audio).
- **Vector store (vector DB / index):** A system that stores vectors + metadata (document id original text, any tags) and supports similarity search (k-NN, ANN).
- **Retriever:** LangChain abstraction that wraps a vector store and returns the top-k similar documents for a query.
- **ANN vs exact search:** Exact search checks all vectors (very accurate but slow on large data), while Approximate Nearest Neighbor (ANN) uses shortcuts (much faster and lighter, with only a tiny accuracy loss).

## Importance of Vector Stores

- Semantic Search: They find information based on meaning, not just exact keywords, so even if we phrase a question differently, we still get the right answer.

- RAG (Retrieval-Augmented Generation): They supply the LLM with the most relevant context, helping it give accurate, fact-based answers instead of guesses.

- Scalability and Speed: With indexing and ANN algorithms, vector stores can handle millions of records while keeping searches quick and efficient.

## Vector Store vs Vector Database

### **Vector Store**
- Typically refers ot a lightweight library or service that focuses on storing vectors (embeddings) and performing similarity search.
- May not include many traditional database features like transactions, rich query languages, or role-based access control.
- Ideal for prototyping, smaller-scale applications.

- E.g., FAISS (Where you store vectors and can query them by similarity, you handle persistence and scaling separately).

### **Vector Database**
- A full-fledged database system designed to store and query vectors.
- Offers additional "database-like" features:
    1. Distributed architecture for horizontal scalling
    2. Durability and persistence (replication, backup/restore)
    3. Metadata handling (schemas, filtes)
    4. Potential for ACID or near ACID guarantees
    5. Authentication/Authorization and more advanced security

- Build for production environments with significan scalling, large datasets.

- E.g., Qdrant, Milvus, Weaviate

### A vector database is effectively a vector store with extra database features (e.g., clustering, scaling, security, metadata filtering and durability)


## Vector Stores in LangChain

- **Supported Stores:** Langchain integrates with miltiple vector stores (FAISS, Pinecone, Chroma, Qdrant, Weaviate etc), giving you flexibility in scale, features, and deployment.
- **Common Interface:** A uniform Vector Store API lets you swap out one backend (e.g., FAISS) for another (e.g., Pinecone) with minimal code changes.
- **Metadata Handling:** Most vector stores in LangChain allow you to attach metadata (e.g., timestamps, authors ) to each document, enabling filter-based retrieval


## **Chroma Vector Store:** Chroma is a lightweight, open-source vector database that is especially friendly for local development and small to medium-scale production needs.

## Working of LangChain
LangChain makes it easy to connect our data with large language models (LLMs). The process usually goes like this:

1. Embeddings Model: Turns text into numeric vectors (embeddings) so the meaning of the text can be compared. LangChain supports many providers like OpenAI, Hugging Face, Cohere and Google.
2. Document Loader and Chunking: Loads our data (PDFs, text, websites, etc.) and breaks it into smaller chunks (usually 500–1,000 tokens) so it can be processed efficiently.
3. Vector Store: Stores these embeddings along with metadata. LangChain can connect to different vector stores like Chroma, FAISS, Pinecone, Weaviate, Qdrant and Milvus.
4. Retriever: Searches the vector store to find the most relevant chunks when we ask a question. These results are then passed to the LLM for generating a final answer.