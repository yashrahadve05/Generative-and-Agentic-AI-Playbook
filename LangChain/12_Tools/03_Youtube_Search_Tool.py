# 03_Youtube_Search_Tool.py

from langchain_community.tools import YouTubeSearchTool

tool = YouTubeSearchTool()


result = tool.run("Explain LangGraph")

print(result)