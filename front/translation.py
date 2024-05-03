import streamlit as st
import requests

translate_url = "http://127.0.0.1:8000/translate"


def translate(text, src_lang, trg_lang):
    """Request summary in summarize_url"""
    response = requests.post(translate_url, json={"text": text, "src": src_lang, "trg": trg_lang})
    translation = response.json()["translation"]
    return translation

st.title("Translation Service")

text = st.text_area("Input any text you want to tranlate", "")

src_lang = st.selectbox("Source Language", ["영어", "한국어", "일본어"])
trg_lang = st.selectbox("Target Language", ["영어", "한국어", "일본어"], index=1)

if st.button("Translate"):
    translated_text = translate(text, src_lang, trg_lang)
    st.success(translated_text)