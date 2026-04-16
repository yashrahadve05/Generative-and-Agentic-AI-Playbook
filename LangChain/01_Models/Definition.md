## What problem does LangChain solve?
Managing multi-step LLM workflows becomes messy:
- Prompt chaining
- Tool calling
- Memory handling

LangChain provides abstractions for:
- Chains → sequential calls
- Agents → decision-making
- Tools → external APIs

## When NOT to use LangChain?
- Simple LLM calls
- When you need full control (better to write custom loop)




---

## Comparisons

### LangChain vs LangGraph

| Feature        |  LangChain        | LangGraph         |
|--------------- |-------------------|-------------------|
| Abstraction    |  High             | Medium            |
| Control        |  Low              | High              |
| Use-case       |  Simple agents    | Complex workflows |