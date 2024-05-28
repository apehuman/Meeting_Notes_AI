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
    st.session_state.messages = [
        {"role": "system", 
         "content": "너는 json으로된 유저의 노트 정보를 받게 될텐데, 너의 업무는 이 노트 정보 안에서 검색해서 말하고, 그 노트가 지금 어떤 노트에 해당하는 내용인지 알려주는거야"}
    ]
    
    st.session_state.messages[0]['content'] += response.text

# Display chat messages from history on app rerun
for message in st.session_state.messages[1:]:
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