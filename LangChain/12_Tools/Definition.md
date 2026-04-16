## **Tools in LangChain :** A tool is just a function (or API) that is packedged in a way the LLM can understand and call when needed. The LLM can call tools to get information, perform actions, or interact with the environment. Tools can be anything from a simple calculator function to a complex API that retrieves data from the web.

In LangChain, tools are defined as classes that inherit from the `BaseTool` class. Each tool must implement the `call` method, which is the function that will be executed when the tool is called by the LLM. The `call` method takes in a string input and returns a string output.

#### **AI Agents :** An AI agent is an LLM-powered system that can autonomously think, decide, and take actions using external tools or APIs to achieve its goals. Agents can use tools to gather information, perform tasks, or interact with the environment to achieve their goals. For example, an agent could use a search tool to find information on the web, a calculator tool to perform calculations, or a database tool to retrieve data from a database.


## **Toolkits in LangChain :** A toolkit is just a conllection (bundle) of related tools that serve a common purpose - packedged together for converience and reusability. For example, a "Web Search Toolkit" might include tools for performing web searches, extracting information from web pages, and summarizing search results. A "Data Analysis Toolkit" might include tools for performing data analysis tasks such as data cleaning, visualization, and statistical analysis.

