import streamlit as st
from langgraph_backend import chatbot
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
    st.session_state['chat_threads'] = []

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
    
    
    CONFIG = RunnableConfig(configurable={'thread_id': st.session_state['thread_id']})
    
    ai_message = ""
    with st.chat_message('assistant'):
        message_area = st.empty()
        for message_chunk, metadata in chatbot.stream(
            {'messages':[HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode='messages'
        ):
            if getattr(message_chunk, 'content', None):
                # extract text from chunk and update display
                chunk_text = message_chunk.content[0].get("text", "") # type: ignore
                ai_message += chunk_text
                message_area.text(ai_message)
    
    
    st.session_state['message_history'].append({'role':'assistant', 'content':ai_message})