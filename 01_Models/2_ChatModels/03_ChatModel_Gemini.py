from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-3.1-pro-preview')

result = model.invoke('What is the capital of India')

print(result.content)



# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-3-flash")

# result = model.invoke("What is the throteling in javascript")

# print(result)