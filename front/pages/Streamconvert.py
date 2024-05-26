import streamlit as st
from st_audiorec import st_audiorec
import os
from shutil import copyfile
import sys
import api
import template
sys.path.append('../')

import audio_process as audio_process

template.base()

# Streamlit 앱의 제목
st.title("녹음 변환기")

if 'conversion_result' not in st.session_state:
    st.session_state['conversion_result'] = "변환 결과가 여기에 표시됩니다."
#녹음중
wav_audio_data = st_audiorec()

# 변환 버튼
if st.button("변환",key="convert_button"):
    
    st.session_state['conversion_result'] = audio_process.audio_process(wav_audio_data)

# 변환 결과를 텍스트 박스에 출력
st.subheader("변환 결과")
st.text_area("conversion_result",value=st.session_state['conversion_result'], height=360 , label_visibility= "hidden")

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
