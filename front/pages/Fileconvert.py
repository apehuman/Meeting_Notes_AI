import streamlit as st
import os
from shutil import copyfile
import sys
import api
import template
sys.path.append('../')

template.base()

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
    import audio_process as audio_process

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
    st.rerun()

# Session state를 사용하여 버튼 클릭 상태를 저장
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# 버튼 클릭 이벤트 처리
def on_button_click():
    pass

if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

if st.button('Save', on_click=on_button_click):
    st.session_state['button_clicked'] = True
    st.session_state['note_content'] = st.session_state['conversion_result']

if st.session_state['button_clicked']:
    title = st.text_input('제목을 입력하세요:', on_change=None)
    if title:
        st.session_state['note_title'] = title

if 'folder_id' not in st.session_state:
    st.switch_page("pages/folders.py")

folder = api.get_folder(st.session_state.folder_id)
st.page_link("pages/folder.py", label=folder['name'], icon="📂")

form = st.form(key="Create Note")
form.markdown("**Add a new Note**")
topic = form.text_input("Add a new topic: ", value=st.session_state.get('note_title', ''))
# 세션 상태에 저장된 변환 결과를 content 필드에 기본값으로 설정
content = form.text_area("Add a new content: ", value=st.session_state.get('note_content', ''))
submit = form.form_submit_button("Add Note")

if submit:
    response = api.create_note(folder['id'], topic, content)
    if(response.status_code == 204):
        st.success(f" '{topic}' note has been added!")
        
                # 노트 추가 후 topic과 content 세션 상태 초기화
        if 'note_title' in st.session_state:
            st.session_state['note_title'] = ''
        if 'note_content' in st.session_state:
            st.session_state['note_content'] = ''
        
        # 성공 메시지 출력 후, 해당 세션 변수들을 초기화
        st.session_state['conversion_result'] = "변환 결과가 여기에 표시됩니다."
    elif(response.status_code == 422):
        st.warning("You should fill the form.")
    elif(response.status_code == 404):
        st.error("There's no such folder")
