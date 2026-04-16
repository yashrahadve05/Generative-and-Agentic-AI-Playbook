## **Retrievers -** A retriever is a component in LangChain that fatches relevant documents from a data source in response to a user's query.

- There are multiple types of retrievers
- All retrievers in LangChain are runnables

## Types of Retrievers

- Data Source
    1. Wikipedia Retrievers: It is a retriever that queries the Wikipedia API to fetch relevant content for a given query.
    2. Vector Store Based Retrievers: A Vector Store Retrieve in LangChain is the most common type of retriever that lets you serch and fetch documents from a vector store based on semantic similarity useing vector embeddings.
    3. Archive Retrievers: These retrievers access archived data to fetch relevant information.
- Search Strategy
    1. Maximal Marginal Relevance (MMR): MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaining high relevance to the query. It works by selecting documents that are not only relevant to the query but also diverse from each other, ensuring a more comprehensive set of results.
    2. Multi-Query Retriever: Sometimes a single query might not capture all the ways information is phrased in you documents. A multi-query retriever generates multiple variations of the original query to increase the chances of retrieving relevant documents that may be phrased differently.
    3. Contextual Compression Retriever: The Contextual Compression Retriever in LangChain is an advanced retriever that improves retrieval quality by compressing the documents after retrieval - keeping only the relevant content based on the user's query. This process helps in reducing noise and enhancing the relevance of the retrieved information, making it more useful for downstream tasks such as question answering or summarization.
    4. Similarity Search: Similarity Search is a retrieval method that identifies and retrieves documents based on their semantic similarity to the user's query. It typically uses vector embeddings to represent both the query and the documents, allowing for a more nuanced understanding of the content and context, which leads to more relevant search results.


