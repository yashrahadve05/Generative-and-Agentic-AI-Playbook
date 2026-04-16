# 01_Wikipedia_Retrievers.py

from langchain_community.retrievers import WikipediaRetriever

retriver = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

query = "The geopolitical history of india and china form the perspective of a US"

# Get relevant Wikipedia documents
docs = retriver.invoke(query)

# Print Retrieved Content
for i, doc in enumerate(docs):
    print(f"\n -- Result {i+1} --")
    print(f"Content: \n {doc.page_content}...") # Truncate for display

