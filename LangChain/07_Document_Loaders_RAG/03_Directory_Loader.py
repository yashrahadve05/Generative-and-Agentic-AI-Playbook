# 03_Directory_Loader.py

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.load()

print(len(docs))

print("Page Content", docs[326].page_content)
print("Metadata", docs[0].metadata)