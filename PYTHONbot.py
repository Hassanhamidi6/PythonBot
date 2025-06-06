from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv
import streamlit as st


# load_dotenv()
# api_key = os.getenv("BotApi")

model = ChatGroq(model="llama-3.3-70b-versatile", api_key="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")


system_prompt = SystemMessage(
    content="""
    You are a helpful assistant specialized only in Python.
    You built by Muhammad Hassan, an Artificial Intelligence developer.
    You only respond to questions related to Python programming (e.g., syntax, libraries, debugging, errors, tips).
    also make your answer simple and user friendly which is easily readable
    If a question is not related to Python, politely respond that you only handle Python-related questions.
    """
)

# Streamlit 
st.title("🐍 Python ChatBot")

# chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display past chat messages using the chat interface
for msg in st.session_state.chat_history:
    with st.chat_message("user" if isinstance(msg, HumanMessage) else "assistant"):
        st.markdown(msg.content)

# Chat input at the bottom
user_input = st.chat_input("Ask a Python question...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add user message to history
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Get bot response
    response = model.invoke([system_prompt] + st.session_state.chat_history)

    # Show bot message
    with st.chat_message("assistant"):
        st.markdown(response.content)

    st.session_state.chat_history.append(response)
