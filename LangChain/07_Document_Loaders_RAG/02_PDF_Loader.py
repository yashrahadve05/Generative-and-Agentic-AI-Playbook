# 02_PDF_Loader.py

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("DL_Syllabus.pdf")

docs = loader.load()

print(len(docs))

print("Page Content: ", docs[0].page_content)
print("Metadata: ", docs[0].metadata)