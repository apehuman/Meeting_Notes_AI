import streamlit as st
import requests

import api


translate_url = "http://127.0.0.1:8000/ai-text/translate"


def _translate(text, src_lang, trg_lang):
    """Request translation from translate_url"""
    response = requests.post(translate_url, 
        json={"text": text, "src": src_lang, "trg": trg_lang})
    translation = response.json()["translation"]
    return translation

@st.experimental_fragment
def translate(note_id, content):
    st.write("어떤 언어로 번역할지 선택해주세요.")
    trg_lang = st.selectbox("Target Language", ["영어", "한국어", "일본어"], index=1)

    if st.button("Translate"):
        translated_text = _translate(content, trg_lang=trg_lang, src_lang="")
        response = api.update_note_translation(note_id, translated_text)
        if response.status_code == 204:
            st.success("해당 노트에 번역이 저장되었습니다.")
            st.write(translated_text)
        else:
            st.error("해당 노트를 찾을 수 없습니다,")
###################################################

summarize_url = "http://127.0.0.1:8000/ai-text/summarize"
summarize_meeting_url = "http://127.0.0.1:8000/ai-text/summarize-meeting"

def summarize(url, text):
    """Request summary in url"""
    response = requests.post(url, json={"text": text})
    summary = response.json()["summary"]
    return summary


@st.experimental_fragment
def summary_3lines(note_id, content):
    if st.button("3줄 요약", key="3line"):
        summary = summarize(summarize_url, content)
        response = api.update_note_summary(note_id, summary)
        if response.status_code == 204:
                st.success("해당 노트에 요약이 저장되었습니다.")
                st.markdown(summary)
        else:
            st.error("해당 노트를 찾을 수 없습니다,")


def make_containers(meeting_summary):
    """Make 3 sections of meeting summary"""
    container1 = st.container(border=True)
    container1.write(meeting_summary[0])
    container2 = st.container(border=True)
    container2.write(meeting_summary[1])
    container3 = st.container(border=True)
    container3.write(meeting_summary[2])

@st.experimental_fragment
def summary_meeting(note_id, content):
    if st.button("회의록 요약", key="meeting"):
        meeting_summary = summarize(summarize_meeting_url, content)
        response = api.update_note_meeting_summary(note_id, meeting_summary)
        if response.status_code == 204:
            st.success("해당 노트에 회의록 요약이 저장되었습니다.")
            meeting_summary = meeting_summary.split('\n\n')
            make_containers(meeting_summary)
        else:
            st.error("해당 노트를 찾을 수 없습니다,")