# 02_Text_Structure_Based_Splitter.py

from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Vector embeddings are numerical representations of data—such as text, images, or audio—converted into lists of numbers (vectors) that capture their semantic meaning. They allow artificial intelligence models to understand relationships, such as identifying that "cat" and "dog" are similar, by placing semantically similar items closer together in a high-dimensional space.
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))

print(chunks)