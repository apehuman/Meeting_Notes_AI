import streamlit as st
import requests

summarize_url = "http://127.0.0.1:8000/ai-text/summarize"
summarize_meeting_url = "http://127.0.0.1:8000/ai-text/summarize-meeting"


def summarize(text, url):
    """Request summary in url"""
    response = requests.post(url, json={"text": text})
    summary = response.json()["summary"]
    return summary

def make_containers(meeting_summary):
    """Make 3 sections of meeting summary"""
    container1 = st.container(border=True)
    container1.write(meeting_summary[0])
    container2 = st.container(border=True)
    container2.write(meeting_summary[1])
    container3 = st.container(border=True)
    container3.write(meeting_summary[2])

def clicked(button):
    """Update the value in session state"""
    st.session_state.clicked[button] = True

# Initialize session state
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "meeting_summary" not in st.session_state:
    st.session_state.meeting_summary = []
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1: False, 2: False}

st.title("Summary Service")

input_text = st.text_area("Input Text", height=300)

st.button("Summarize", on_click=clicked, args=[1])
if st.session_state.clicked[1]:
    if input_text:
        if st.session_state.summary:                # read session state
            st.success(st.session_state.summary)
        else: 
            try:
                summary = summarize(input_text, summarize_url)
            except:                         # if bad response
                st.error("Request Error")
            else: 
                st.success(summary)
                st.session_state.summary = summary  # memorize in session state
    else:                                   # if no input text
        st.warning("Please Enter Text")
# ---------------------------------------------------------------------------
st.button("Summarize meeting", on_click=clicked, args=[2])
if st.session_state.clicked[2]:
    if input_text:
        if st.session_state.meeting_summary:       # read session state
            make_containers(st.session_state.meeting_summary)
        else: 
            try:
                meeting_summary = summarize(input_text, summarize_meeting_url)
            except:                         # if bad response
                st.error("Request Error")
            else:
                meeting_summary = meeting_summary.split('\n\n')
                make_containers(meeting_summary)
                for section in meeting_summary:    # memorize in session state
                    st.session_state.meeting_summary.append(section)
    else:                               # if no input text
        st.warning("Please Enter Text")