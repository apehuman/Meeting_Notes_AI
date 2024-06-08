import streamlit as st
import requests
import json

import api
import template

template.base()

chat_url = "http://127.0.0.1:8000/ai-text/chat"

st.title("ChatGPT-like clone")


def get_user_info(username):
    user_url = f"http://127.0.0.1:8000/user/{username}"
    return requests.get(user_url)
response = get_user_info(st.session_state.username)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Say something"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        messages = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        response = requests.post(chat_url, json=dict(messages = messages))
        st.markdown(response.json()["content"])
        # Add assistant response to chat history
        st.session_state.messages.append(response.json())