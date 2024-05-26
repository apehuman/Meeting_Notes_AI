import streamlit as st
import os
from shutil import copyfile

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

# 중앙에 파일 업로드 섹션을 배치
uploaded_file = st.file_uploader("여기에 mp4, m4a, mp3, amr, flac, wav 파일을 드래그 앤 드롭하거나 업로드 버튼을 클릭하세요.", type=['mp4', 'm4a', 'mp3', 'amr', 'flac', 'wav'])
st.markdown('</div>', unsafe_allow_html=True)

# 업로드된 파일이 있을 때 변환 버튼과 결과 출력
if uploaded_file is not None:
    # 음성 변환 함수 호출
    import audio_process

    # 변환 버튼
    if st.button("변환", key="convert_button"):
        # 파일을 처리하여 변환 결과 얻기
        st.session_state['conversion_result'] = audio_process.audio_process(uploaded_file)
else:
    st.write("WAV 파일을 업로드해주세요.")

# 변환 결과를 텍스트 박스에 출력
st.subheader("변환 결과")
st.text_area("변환 결과", value=st.session_state['conversion_result'], height=360)

# 초기화 버튼
if st.button("초기화"):
    st.session_state['conversion_result'] = "변환 결과가 여기에 표시됩니다."
    st.session_state.button_clicked = False
    st.experimental_rerun()


# Session state를 사용하여 버튼 클릭 상태를 저장
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# 버튼 클릭 이벤트 처리
def on_button_click():
    st.session_state.button_clicked = True

# 버튼을 클릭했는지 확인
if st.button('저장', on_click=on_button_click):
    st.session_state.button_clicked = True

# 버튼 클릭 후 텍스트 입력 필드와 입력값 처리
if st.session_state.button_clicked:
    title = st.text_input('제목을 입력하세요:', on_change=None)
    if title:
        st.write(f'입력한 제목: {title}')
         #제목값은 title , 전사 결과는 st.session_state['conversion_result']