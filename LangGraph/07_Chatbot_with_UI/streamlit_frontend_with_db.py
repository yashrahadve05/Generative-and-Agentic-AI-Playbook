import streamlit as st
from langgraph_backend_with_db import chatbot, retrieve_all_threads
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

import uuid


# ******************************** Utility Functions ******************************** # 

def generate_thread_id():
    thread_id = uuid.uuid4()
    
    return thread_id


def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    state =  chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    print(state.values)

    return state.values.get('messages', [])

# ******************************** Session Setup ******************************** # 
# st.session_state -> dict
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

add_thread(st.session_state['thread_id'])

# ******************************** Sidebar UI ******************************** # 

st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversations")

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        
        
        # **** For OpenAI Response **** #
        # temp_messages = []
        
        # for msg in messages:
        #     if isinstance(msg, HumanMessage):
        #         role = 'user'
        #     else:
        #         role = 'assistant'
            
        #     temp_messages.append({'role': role, 'content': msg.content})
        
        
        # **** For Gemini Response **** #
        temp_messages = []

        for msg in messages:
            role = "user" if isinstance(msg, HumanMessage) else "assistant"

            if isinstance(msg.content, str):
                text = msg.content
            elif isinstance(msg.content, list):
                text = "".join(
                    block.get("text", "")
                    for block in msg.content
                    if isinstance(block, dict) and block.get("type") == "text"
                )

            else:
                text = str(msg.content)

            temp_messages.append({
                "role": role,
                "content": text
            })
        
        st.session_state['message_history'] = temp_messages


# ******************************** Main UI ******************************** # 
# Loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])




user_input = st.chat_input('Type here...')

if user_input:
    
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
    
    
    # CONFIG = RunnableConfig(configurable={'thread_id': st.session_state['thread_id']})
    
    CONFIG = RunnableConfig(
        configurable={"thread_id": st.session_state["thread_id"]},
        metadata={"thread_id": st.session_state["thread_id"]},
        run_name="chat_turn"
    )
    
    ai_message = ""
    with st.chat_message('assistant'):
        message_area = st.empty()
        for message_chunk, metadata in chatbot.stream(
            {'messages':[HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode='messages'
        ):
            # 1. Handle case where chunk is just a raw string
            if isinstance(message_chunk, str):
                ai_message += message_chunk
                message_area.markdown(ai_message)
                
            # 2. Handle AIMessageChunk objects (Standard for LangChain Gemini)
            elif hasattr(message_chunk, 'content'):
                content = message_chunk.content
                
                # Check for standard string content (Most common Gemini chunk payload)
                if isinstance(content, str) and content:
                    ai_message += content
                    message_area.markdown(ai_message)
                
                # Safely handle list/multimodal block content variations
                elif isinstance(content, list) and len(content) > 0:
                    first_block = content[0]
                    
                    if isinstance(first_block, dict):
                        chunk_text = first_block.get("text", "")
                    elif isinstance(first_block, str):
                        chunk_text = first_block
                    else:
                        chunk_text = getattr(first_block, "text", str(first_block))
                        
                    ai_message += chunk_text
                    message_area.markdown(ai_message)
