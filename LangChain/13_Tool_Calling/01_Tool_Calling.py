# 01_Tool_Calling.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage, HumanMessage
import requests as req

from dotenv import load_dotenv


load_dotenv()


# Create Tool
@tool
def multiply(a: int, b: int) -> int:
    """Given 2 number a and b this tool returns their product"""
    return a * b


print(multiply.invoke({'a': 3, 'b': 4}))

# To get the name
print(multiply.name)

# To get the description
print(multiply.description)

# To get the arguments passed with tool
print(multiply.args)


# Tool Binding

llm = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

llm_with_tools = llm.bind_tools([multiply])



# Tool Calling - Asking Random Qestion
# print(llm_with_tools.invoke("Hey, Which Model You are!"))

query = HumanMessage("Can you please multiply 4 with 9")

messages: list[BaseMessage] = [query]

# Asking Question that need to call tools
# print(llm_with_tools.invoke("Can you please multiply 7 with 9").tool_calls[0])

result = llm_with_tools.invoke(messages)

messages.append(result)

tool_message = multiply.invoke(result.tool_calls[0])

messages.append(tool_message)

# Final Result
print(llm_with_tools.invoke(messages).content)