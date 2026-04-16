# 01_Search_Tool.py

from langchain_community.tools import DuckDuckGoSearchRun


search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke("What is LangGraph")

print(results)
