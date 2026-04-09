# # 04_ChatModel_HF_API.py


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage # Import this!
from dotenv import load_dotenv

load_dotenv()

# Use a model that is fully supported by the Chat Inference API
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
    task="text-generation",
    max_new_tokens=512,
    temperature=0.5,
)

model = ChatHuggingFace(llm=llm)

# Passing a list of messages is the correct way for ChatModels
messages = [
    HumanMessage(content="What is debouncing in javascript?")
]

result = model.invoke(messages)

print(result.content)



# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm = llm)

# result = model.invoke("What is the Debouncing in javascript!")

# print(result.content)