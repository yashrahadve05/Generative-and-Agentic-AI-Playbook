

## Memory store = 

## namespace => It is a hierarchical path (like a folder-like structure of strings) used to logically organize and isolate data within long-term memory. It allows your agent to store, retrieve, and search information (like preferences, user facts, or past experiences) across different conversation threads.

## Put => It inserts the new memory in a particular namespace, basically it is user for creating new memory. It is a method to store information in the long-term memory. It takes a namespace, a unique key, and the data to be stored. The data can be any JSON-serializable object.
- It needs 2 things: 
  - namespace: A string that represents the hierarchical path where the memory will be stored.
  - key: A unique identifier for the memory entry within the specified namespace.
  - data: The actual information to be stored, which can be any JSON-serializable object.