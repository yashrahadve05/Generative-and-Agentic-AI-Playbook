from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5-2025-08-07")

result = model.invoke("Explain Debouncing in javascript")


print(result.content)

