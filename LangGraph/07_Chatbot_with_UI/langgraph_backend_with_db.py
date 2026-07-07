from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

import sqlite3
import os


load_dotenv()

llm = ChatGoogleGenerativeAI( model= "gemini-3.1-flash-lite")

# 1. Setup Database & Automatically Create Missing Folders
db_path = './chatbot.db'
os.makedirs(os.path.dirname(db_path), exist_ok=True)


connection = sqlite3.connect(db_path, check_same_thread=False)
checkpoint = SqliteSaver(conn=connection)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}


graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpoint)

def retrieve_all_threads():
    all_threads = set()
    
    for cp in checkpoint.list(None):
        # configurable may not be present; guard against missing keys
        configurable = cp.config.get('configurable') if isinstance(cp.config, dict) else None
        if configurable and isinstance(configurable, dict):
            thread_id = configurable.get('thread_id')
            
            if thread_id:
                all_threads.add(thread_id)
    
    return list(all_threads)

# response = chatbot.invoke(
#     {'messages': [HumanMessage(content="Hey, I am Yash")]},
#     config={'configurable': {'thread_id': 'thread-1'}}
# )

# print(response)