import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("BotApi")

# Initialize the model
model = ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)

# Define the system prompt
system_prompt = SystemMessage(
    content='''
        You are an intelligent and creative rhyme maker, designed to craft rhymes for given words, 
        and compose poetic verses or lyrical content. Your purpose is to assist in the art of rhyming, 
        especially for songs and poems.

        You were developed by Hassan Hamidi, an AI developer with a passion for language and creativity.

      
        You are strictly focused on rhyming tasks—creating rhymes, generating poems, and lyrical content. 
        If a user asks a question unrelated to rhyming or poetry, politely inform them that you only handle 
        rhyme-related queries for poems and songs.

        Stay creative. Stay on rhyme.

        If a user gves you any English or urdu word try your best to give them the best rhyming word 
        related to that 
    '''
)

# Function to get the model response
def get_response(query):
    response = model.invoke([
        system_prompt, HumanMessage(query)
    ])
    return response.content

# Streamlit UI
st.set_page_config(page_title="🎤 Rhyme Maker Bot", page_icon="🎶")

st.title("🎶 Rhyme Maker Bot")
st.subheader("Crafting rhymes and poetic lines, powered by Hassan Hamidi's AI")

with st.form("rhyme_form"):
    user_input = st.text_area("Enter your word, line, or poem idea:", height=150)
    submit = st.form_submit_button("Generate Rhyme")

if submit and user_input.strip():
    with st.spinner("Thinking in rhymes... 🎵"):
        output = get_response(user_input)
        st.markdown("### ✨ Here's your rhyme:")
        st.write(output)
