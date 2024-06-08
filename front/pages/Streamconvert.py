import audio_process as audio_process
import streamlit as st
from st_audiorec import st_audiorec
import os
from shutil import copyfile
import sys
import api
import template
sys.path.append('../')


template.base()

if 'username' not in st.session_state:
    st.switch_page("pages/user_login.py")

else:
    if 'folder_id' not in st.session_state:
        st.session_state['folder_id'] = 1

# Streamlit 앱의 제목
st.title("녹음 변환기")


# 변환 결과를 위한 상태 변수 초기화
if 'conversion_result' not in st.session_state:
    st.session_state['conversion_result'] = "변환 결과가 여기에 표시됩니다."

# 변환 형식을 위한 상태 변수 초기화
if 'transcribe_mode' not in st.session_state:
    st.session_state['transcribe_mode'] = 'transcription'

# 모드 선택 라디오 버튼
mode = st.radio("결과 형식 선택", ('일반 발화', '회의록'))

# 모드 선택에 따라 상태 변수 업데이트
if mode == '일반 발화':
    st.session_state['transcribe_mode'] = 'transcription'
    print(st.session_state['transcribe_mode'])
elif mode == '회의록':
    st.session_state['transcribe_mode'] = 'conversation'
    print(st.session_state['transcribe_mode'])

# 녹음중
wav_audio_data = st_audiorec()

# 변환 버튼
if st.button("변환", key="convert_button"):

    st.session_state['conversion_result'] = audio_process.audio_process(
        wav_audio_data, st.session_state['transcribe_mode'])

# 변환 결과를 텍스트 박스에 출력
st.subheader("변환 결과")
st.text_area("conversion_result",
             value=st.session_state['conversion_result'], height=360, label_visibility="hidden")

# Session state를 사용하여 버튼 클릭 상태를 저장
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# 버튼 클릭 이벤트 처리


def on_button_click():
    pass


if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

# 초기화 버튼
col1, col2 = st.columns(2)

with col1:
    if st.button("초기화"):
        st.session_state['conversion_result'] = "변환 결과가 여기에 표시됩니다."
        st.session_state.button_clicked = False
        st.rerun()

with col2:
    if st.button('Save'):
        st.session_state['button_clicked'] = True
        st.session_state['note_content'] = st.session_state['conversion_result']
        st.switch_page("pages/new_note_form.py")