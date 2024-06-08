import streamlit as st
import os
from shutil import copyfile
import sys
import api
import template
sys.path.append('../')

template.base()

if 'username' not in st.session_state:
    st.switch_page("pages/user_login.py")

if 'folder_id' not in st.session_state:
    st.session_state['folder_id'] = 1

# Streamlit 앱의 제목
st.title("음성파일 변환기")

# 스타일 정의
st.markdown("""
    <style>
    .main-button {
        position: fixed;
        top: 10px;
        left: 10px;
        background-color: #3498db;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 5px;
        z-index: 1000;
    }        
    .convert-button {
        background-color: #4CAF50; /* Green */
        color: black;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

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

# 중앙에 파일 업로드 섹션을 배치
uploaded_file = st.file_uploader("여기에 mp4, m4a, mp3, amr, flac, wav 파일을 드래그 앤 드롭하거나 업로드 버튼을 클릭하세요.", type=[
                                 'mp4', 'm4a', 'mp3', 'amr', 'flac', 'wav'])
st.markdown('</div>', unsafe_allow_html=True)

# 업로드된 파일이 있을 때 변환 버튼과 결과 출력
if uploaded_file is not None:
    # 음성 변환 함수 호출
    import audio_process as audio_process

    # 변환 버튼
    if st.button("변환", key="convert_button"):
        # 파일을 처리하여 변환 결과 얻기
        st.session_state['conversion_result'] = audio_process.audio_process(
            uploaded_file, st.session_state['transcribe_mode'])
else:
    st.write("WAV 파일을 업로드해주세요.")

# 변환 결과를 텍스트 박스에 출력
st.subheader("변환 결과")
st.text_area("변환 결과", value=st.session_state['conversion_result'], height=360)

# Session state를 사용하여 버튼 클릭 상태를 저장
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# 버튼 클릭 이벤트 처리


def on_button_click():
    pass


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