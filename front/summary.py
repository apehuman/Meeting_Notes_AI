import streamlit as st
import requests

summarize_url = "http://127.0.0.1:8000/summarize"


def summarize(text):
    """Request summary in summarize_url"""
    response = requests.post(summarize_url, json={"text": text})
    summary = response.json()["summary"]
    return summary


st.title("Summary Service")

input_text = st.text_area("Input Text", height=300)
if st.button("Summarize"):
    if input_text:
        try:
            summary = summarize(input_text)
            st.success(summary)
        except:                         # if bad response
            st.error("Request Error")
    else:                               # no input text
        st.warning("Please Enter Text")