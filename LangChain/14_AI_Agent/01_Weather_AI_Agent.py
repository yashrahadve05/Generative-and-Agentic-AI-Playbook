# 01_Weather_AI_Agent.py


import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langsmith import Client
from dotenv import load_dotenv


load_dotenv()


search_tool = DuckDuckGoSearchRun()


# Step 1: Create a custom tool to fetch weather data from weatherapi
@tool
def get_weather_data(city: str):
    """This function(tool) fetch the current weather data for given city form weatherapi """

    url = f'http://api.weatherapi.com/v1/current.json?key=a5de70e2050445bebf8212912262301&q={city}&aqi=no'
    
    response = requests.get(url)

    return response


llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)

# Step 2: Pull the ReAct prompt from LangChain Hub
client = Client()
prompt = client.pull_prompt("hwchase17/react")  # pulls the standard ReAct agent prompt


# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

# Step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)

# Step 5: Invoke
response = agent_executor.invoke({"input": "Find the capital of Madhya Pradesh, then find it's current weather condition"})

print("Response", response)
print("Agent execution completed!", response["output"])