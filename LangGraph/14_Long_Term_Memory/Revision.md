# Long-Term Memory in LangGraph (Complete Revision Notes)


## Overview

Large Language Models (LLMs) are **stateless**.

Every API call is independent unless previous conversation history is provided.

This creates a major limitation:

* The model forgets users.
* User preferences are lost.
* Every new chat starts from scratch.

LangGraph solves this by introducing **Long-Term Memory**, allowing an AI application to remember users across multiple conversations.

Think of it exactly like ChatGPT remembering your name, profession, projects, and preferences.

---

# Why Do We Need Long-Term Memory?

Suppose a user says:

> My name is Yash.

Later, in another conversation, they ask:

> Suggest a backend project.

Without long-term memory:

```
Who are you?
```

The model has forgotten.

With long-term memory:

```
Hi Yash,

Since you're interested in backend engineering...
```

The AI becomes personalized.

---

# Short-Term Memory vs Long-Term Memory

| Short-Term Memory             | Long-Term Memory             |
| ----------------------------- | ---------------------------- |
| Exists only inside one chat   | Exists across multiple chats |
| Stored in Checkpointer        | Stored in Memory Store       |
| Deleted when thread ends      | Permanent                    |
| Used for current conversation | Used for personalization     |
| Thread Scoped                 | Cross Thread                 |
| Temporary                     | Persistent                   |

Example:

```
Chat Thread 1

Hi
My name is Yash
↓
Close chat
↓
Open new chat
↓
Who am I?
```

Without long-term memory:

```
I don't know.
```

With long-term memory:

```
You are Yash.
```

---

# How Long-Term Memory Works

The overall workflow is:

```
          User
             │
             ▼
      User Message
             │
             ▼
      Remember Node
             │
   Extract Important Facts
             │
             ▼
      Memory Store
             │
             ▼
      Semantic Search
             │
             ▼
      Chat Node
             │
             ▼
      Personalized Response
```

The chatbot performs **two independent tasks**:

1. Save important information.
2. Retrieve relevant information.

---

# Memory Store

A Memory Store is simply a database that stores user memories.

Instead of saving conversations, we save **facts**.

Example

Instead of storing:

```
Hello

How are you?

Fine

What's your name?
```

We store:

```
Name = Yash

Profession = Software Engineer

Favorite Language = JavaScript

Working On = AI Platform
```

This makes retrieval much easier.

---

# BaseStore

LangGraph introduces an abstract class called **BaseStore**.

It defines the common operations every memory store must support.

Typical operations include:

* Put
* Get
* Search
* Delete
* Update

Different storage implementations inherit this interface, such as in-memory or PostgreSQL-backed stores. ([LangChain Blog][2])

---

# InMemory Store

```
RAM
```

Characteristics

* Fast
* Easy to use
* Perfect for development
* Data disappears after restart

Example

```
Restart Application

↓

Everything Lost
```

Therefore it should never be used in production.

---

# PostgreSQL Store

Instead of RAM:

```
RAM

↓

Database

↓

PostgreSQL
```

Advantages

* Persistent
* Survives restart
* Production Ready
* Scalable
* Reliable

---

# Namespace

Namespaces organize memories.

Think of them like folders.

Example

```
users/

      Yash/

            profile

            preferences

            projects
```

Instead of storing everything together:

```
Database

Name

Language

Food

Movies

Projects

Age

Skills
```

Namespaces isolate user data.

Example

```
users

     user1

     user2

     user3
```

Each user gets independent memory.

---

# Why Namespace Is Important

Without namespaces:

```
Database

John

Yash

Alice

Rahul
```

The chatbot cannot determine ownership.

With namespaces:

```
users/

      Yash/

            name

            project

            language
```

Everything remains isolated.

---

# Semantic Search

Imagine the memory contains:

```
Favorite Food

Favorite Movie

Favorite Language

Current Project

Travel Plans

College
```

User asks:

```
Help me in my AI project.
```

Should we send all memories?

No.

That wastes tokens.

Instead we retrieve only relevant memories.

```
AI Project

↓

Current Project

↓

Favorite Language
```

Semantic Search uses embeddings to retrieve the most relevant information instead of exact keyword matches. This improves efficiency and response quality. ([YouTubeSummary][1])

---

# Embeddings

Every memory becomes a vector.

Example

```
I love JavaScript.

↓

Embedding

↓

[0.24,0.93,0.18....]
```

User query

```
Recommend backend framework.
```

↓

Embedding

↓

Similarity Search

↓

Returns

```
Favorite Language = JavaScript
```

The chatbot can now recommend:

```
Express

NestJS

Fastify
```

because it understands the semantic meaning rather than matching words literally.

---

# Memory Retrieval

Whenever a user sends a message:

```
User Query

↓

User ID

↓

Namespace

↓

Semantic Search

↓

Relevant Memories

↓

LLM
```

Only the relevant memories are injected into the prompt.

---

# User ID

LangGraph retrieves the user ID from the graph configuration.

Example

```
configurable

user_id

↓

Yash
```

Then memory is searched only inside

```
users/Yash
```

This prevents one user's memories from leaking into another user's responses.

---

# Chat Node

The Chat Node performs three steps:

### Step 1

Receive user message.

### Step 2

Retrieve memories.

### Step 3

Inject memories into the system prompt.

Example

```
System Prompt

You know the following facts about the user

Name = Yash

Language = JavaScript

Project = AI Platform
```

Then the LLM generates a personalized response.

---

# Remember Node

This node decides what should be stored.

Not every sentence is useful.

Example

User says

```
Hello
```

Do not save.

User says

```
My name is Yash.
```

Save.

User says

```
I love JavaScript.
```

Save.

User says

```
Thank you.
```

Ignore.

The Remember Node acts as an intelligent memory filter.

---

# Memory Extraction Using LLM

Instead of using rules,

```
if contains "name"
```

we let another LLM decide.

Example

Input

```
My name is Yash.

I am building an AI Industrial Platform.

I love JavaScript.
```

Output

```
Name

Yash

Profession

Software Engineer

Project

AI Platform

Favorite Language

JavaScript
```

Only stable, user-specific facts are extracted and stored.

---

# Pydantic Structured Output

Instead of free text,

the LLM returns structured JSON.

Example

```python
{
    "should_store": true,
    "memories": [
        {
            "type":"project",
            "value":"AI Industrial Platform"
        }
    ]
}
```

Advantages

* Predictable
* Easy parsing
* Type-safe
* Less hallucination
* Easier validation

---

# Duplicate Memory Problem

Suppose the user repeatedly says

```
My name is Yash.
```

Without deduplication

Database

```
Yash

Yash

Yash

Yash

Yash
```

This wastes storage and hurts retrieval quality.

---

# Deduplication Solution

Before writing new memory

```
Extract Memory

↓

Search Existing Memory

↓

Already Exists?

↓

Yes

↓

Skip

↓

No

↓

Store
```

The tutorial uses the LLM itself to compare new information against existing memories and only store genuinely new facts. ([YouTubeSummary][1])

---

# Complete Workflow

```
                User

                  │

                  ▼

          User Message

                  │

                  ▼

          Remember Node

                  │

     Extract Important Facts

                  │

                  ▼

          Duplicate Check

                  │

          New Memory?

          │          │

         No         Yes

          │          │

          ▼          ▼

        Ignore    Store Memory

                     │

                     ▼

              Memory Store

                     │

                     ▼

            Semantic Search

                     │

                     ▼

               Chat Node

                     │

                     ▼

           Personalized Reply
```

---

# Why InMemory Store Is Not Production Ready

Suppose

```
Store Name

↓

Restart Server
```

Memory becomes

```
Empty
```

Every restart wipes the data.

---

# Production Setup

Use

```
Docker

↓

PostgreSQL

↓

LangGraph PostgreSQL Store

↓

Persistent Database
```

Benefits

* Survives server restart
* Persistent storage
* Multiple users
* Production deployment
* Scalable architecture

---

# Real Production Architecture

```
                User

                  │

                  ▼

             LangGraph

                  │

      ┌───────────┴────────────┐

      ▼                        ▼

Remember Node            Chat Node

      │                        │

      ▼                        ▼

PostgreSQL Store ← Semantic Search

      │

      ▼

Persistent User Memory
```

---

# Advantages of Long-Term Memory

* Personalized conversations
* Cross-session memory
* Better recommendations
* Improved user experience
* Reduced repetitive questions
* Scalable architecture
* Production-ready AI assistants
* Context-aware responses
* Efficient memory retrieval through semantic search
* Persistent storage across application restarts

---

# Key Interview Questions

### What is Long-Term Memory?

Persistent storage that enables an AI system to remember information across multiple conversations.

---

### Difference between Short-Term and Long-Term Memory?

Short-term memory is thread-specific and temporary, whereas long-term memory persists across threads and sessions.

---

### What is Namespace?

A logical grouping mechanism used to isolate memories for different users or applications.

---

### Why is Semantic Search required?

It retrieves only the memories relevant to the current query instead of loading every stored memory, reducing token usage and improving relevance.

---

### Why not use InMemory Store in production?

Because all stored data is lost when the application restarts.

---

### Why PostgreSQL?

It provides persistent, scalable, and reliable storage suitable for production deployments.

---

### Why use Pydantic Structured Output?

It forces the LLM to produce structured, validated data that can be stored reliably.

---

### What is Deduplication?

The process of preventing duplicate facts from being stored multiple times in the memory database.

---

# Final Revision Summary

* LLMs are stateless by default.
* Long-term memory enables personalization across conversations.
* Memory is stored in a **Memory Store**, not the conversation history.
* **Namespaces** isolate memories for each user.
* **Semantic Search** retrieves only the most relevant memories.
* The **Remember Node** extracts important user facts.
* **Pydantic Structured Outputs** provide structured memory extraction.
* **Deduplication** prevents redundant memories.
* **InMemory Store** is suitable only for development.
* **PostgreSQL Store** is recommended for production because it provides persistent storage.
* The complete workflow combines memory extraction, storage, semantic retrieval, and personalized response generation to create intelligent, user-aware AI applications. ([YouTubeSummary][1])

[1]: https://youtubesummary.com/summary/KrXBcokM3Tc "Video Summary - Long Term Memory in LangGraph"
[2]: https://blog.langchain.dev/launching-long-term-memory-support-in-langgraph/ "Launching Long-Term Memory Support in LangGraph"
