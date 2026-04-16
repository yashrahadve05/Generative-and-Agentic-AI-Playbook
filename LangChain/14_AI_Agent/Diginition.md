## **AI Agent -** An AI agent is an intelligent system that receives a high-level goal from a user, and autonomously plans, decides, and executes a sequence of actions by using external tools, APIs, or knowledge sources - All while maintaning context, reasoning over multiple steps, adapting to new information, and optimizing for the intended outcome.

### **Key Characteristics of AI Agents:**
1. **Goal Oriented :** AI agents are designed to achieve specific objectives or goals set by users.
2. **Autonomous :** They operate independently, making decisions and taking actions without constant human intervention.
3. **Context-Aware :** AI agents maintain an understanding of the context in which they operate, allowing them to make informed decisions.
4. **Tool Utilization :** They can leverage external tools, APIs, and knowledge sources to enhance their capabilities and achieve their goals effectively.
5. **Multi-Step Reasoning :** AI agents can reason over multiple steps, allowing them to solve complex problems that require a sequence of actions.
6. **Adaptability :** They can adapt to new information and changing circumstances, adjusting their plans and actions accordingly.


### **ReAct Framework -** ReAct (Reasoning and Acting) is a design pattern used in AI agents, It allows a LLM to use internal reasoning (Thought) with external action (like tool use) in a structured, multi-step process. The ReAct framework consists of three main components:
1. **Thought :** The internal reasoning process where the agent generates insights, plans, and makes decisions based on the current context and information available.
2. **Action :** The external execution phase where the agent performs actions, such as calling APIs, using tools, or interacting with the environment to achieve its goals.
3. **Observation :** The feedback loop where the agent observes the outcomes of its actions, allowing it to learn, adapt, and refine its reasoning and actions in subsequent steps.


#### Insted of generating an answer in one go, the model thinks step by step, deciding what is needs to do next and optionally calling tools (APIs, like web search, currecny conversion, etc.) to help it. This allows the model to solve more complex problems that require multiple steps of reasoning and action, and also to adapt to new information as it becomes available.

### **ReAct is Usefull for**
- Multi-step reasoning tasks
- Tool augmened tasks (web search, database lookup, etc.)
- Making the agent's geasoning transparent and autitalbe


## **Agent & Agent Executor**

`AgentExecutor` orchestrates the entire loop:
1. Sends input and previous messages to the agent (LLM).
2. Gets the next `action` from the agent
3. Executes the tool with provided input and gets the `observation`
4. Add the tool's `observation` back into the message history.
5. Repeats the process until the agent returns a final answer (instead of an action).


### **Creating an Agent**

```python
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, calculator_tool],
    prompt=prompt_template,
)
```

### **Creating an Agent Executor**

```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, calculator_tool],
    verbose=True,
)
agent_executor.run("What is the current population of Indor City?")
```