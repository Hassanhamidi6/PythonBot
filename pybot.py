    from langchain_groq import ChatGroq
    from langchain_core.messages import SystemMessage, HumanMessage
    import streamlit as st
    from dotenv import load_dotenv
    import os


    load_dotenv()
    api_key=os.getenv("BotApi")

    model=ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)


    system_prompt=SystemMessage(
        content=(
            '''
            You are a helpful assistant specializied only in python.You are design only responsd to teh querries 
            that are related to the python prgramming language including syntax, libraries, errors, debugging, and best practices.
            If a question is not related to the python just poiltely resposne them that you are design to answer only python questions
    '''
        )
    )


    def get_response(query):
        response=model.invoke([
            system_prompt , HumanMessage(query)
        ])
        return response.content

    while True:
        query=input("Enter your query: ")
        if query=="exit":
            break
        print(get_response(query))


