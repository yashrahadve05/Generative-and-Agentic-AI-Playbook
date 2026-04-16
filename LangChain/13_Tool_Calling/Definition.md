## **Tool Calling -** This is the process where the LLM (Language Model) decides, during a conversation or task, that it needs to use a specific tool or function and generates a structured output with:
1. **Tool Name**: The identifier for the tool it wants to use.
2. **Arguments**: The necessary parameters or inputs required by the tool to perform its function 

The LLM does not actually run the tool itself -> It just suggests the toll and the input argumnets. The actual execution is handled by LangChain or the system that integrates the LLM.


### **Tool Binding -** Tool Binding is the step where you register tools with a LLM so that:
1. The LLM is aware of what tools are available for it to call.
2. It know what each tool does (via description)
3. It knows what input format to use (via schema)

## **Tool Execution -** Tool Execution is the step where the actual Python function (tool) is executed and uses input arguments that the LLM suggested during the Tool Calling Phase.

In summary:
- **Tool Calling**: LLM decides to use a tool and generates the tool name and arguments.
- **Tool Binding**: You register tools with the LLM, providing descriptions and input schemas.
- **Tool Execution**: The registered tool is executed with the arguments provided by the LLM during the Tool Calling phase.
