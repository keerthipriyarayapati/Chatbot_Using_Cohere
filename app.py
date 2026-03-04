## Conversational Q&A Chatbot

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatCohere

# Load environment variables
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# Initialize Cohere chat model
chat = ChatCohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    temperature=0.5
)

# Store conversation history
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant")
    ]

# Function to get chatbot response
def get_chatmodel_response(question):
    
    st.session_state['flowmessages'].append(
        HumanMessage(content=question)
    )

    answer = chat.invoke(st.session_state['flowmessages'])

    st.session_state['flowmessages'].append(
        AIMessage(content=answer.content)
    )

    return answer.content


# User input
user_input = st.text_input("Input:", key="input")

# Button
submit = st.button("Ask the question")

# Generate response only after button click
if submit and user_input:
    response = get_chatmodel_response(user_input)

    st.subheader("The Response is")
    st.write(response)