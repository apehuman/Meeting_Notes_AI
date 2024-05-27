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

# @st.experimental_fragment
def translate(note_id, content):
    st.write("어떤 언어로 번역할지 선택해주세요.")
    trg_lang = st.selectbox("Target Language", ["영어", "한국어", "일본어"], index=1)

    if st.button("Translate"):
        translated_text = _translate(content, trg_lang=trg_lang, src_lang="")
        response = api.update_note_translation(note_id, translated_text)
        if response.status_code == 204:
            st.success("해당 노트에 번역이 저장되었습니다.")
        else:
            st.error("해당 노트를 찾을 수 없습니다,")
        st.write(translated_text)
