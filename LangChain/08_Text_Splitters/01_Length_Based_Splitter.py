# 01_Length_Based_Splitter.py

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# text = """
# MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems.
# Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks.
# Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

# What can MCP enable?
# Agents can access your Google Calendar and Notion, acting as a more personalized AI assistant.
# Claude Code can generate an entire web app using a Figma design.
# Enterprise chatbots can connect to multiple databases across an organization, empowering users to analyze data using chat.
# AI models can create 3D designs on Blender and print them out using a 3D printer.​
# """

loader = PyPDFLoader("DL_Syllabus.pdf")

docs = loader.load()


splitter = CharacterTextSplitter(
    chunk_size = 60,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_documents(docs)

print(result[1].page_content)