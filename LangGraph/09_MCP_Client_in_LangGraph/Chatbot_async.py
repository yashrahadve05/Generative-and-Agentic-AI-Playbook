from pyexpat.errors import messages
from sre_parse import State

from langgraph.graph import StateGraph, START
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool

import asyncio

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div
    """
    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}
        
        return {"first_num": first_num, "second_num": second_num, "operation": operation, "result": result}
    except Exception as e:
        return {"error": str(e)}

tools = [calculator]

llm_with_tools = llm.bind_tools(tools)


# Add State
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# Build Graph

def build_graph():
    
    # Node
    async def chat_node(state: ChatState):
        messages = state['messages']
        response = await llm_with_tools.ainvoke(messages)
        
        return {'messages': [response]}
    
    tool_node = ToolNode(tools)
    
    # Defining graph and nodes
    graph = StateGraph(ChatState)
    
    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)
    
    # Difining graph connections with edges
    graph.add_edge(START, "chat_node")
    graph.add_conditional_edges("chat_node", tools_condition)
    graph.add_edge("tools", "chat_node")
    
    chatbot = graph.compile()
    
    
    return chatbot

async def main():
    
    chatbot = build_graph()
    
    # Running the graph
    result = await chatbot.ainvoke({'messages': [HumanMessage(content="Explain what AI Engineer does and I can say a combination of Full Stack developer + Data Science can become an AI Engineer.")]})

    print(result['messages'][-1].content[0]['text'])


if __name__ == '__main__':
    asyncio.run(main())