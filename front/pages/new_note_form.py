import streamlit as st

import ai_text
import api
import template

template.base()

if 'username' not in st.session_state:
    st.switch_page("pages/user_login.py")

else:
    if 'folder_id' not in st.session_state:
        st.session_state['folder_id'] = 1

user = api.get_user_info(st.session_state.username)
folders = user['folders']
folder_names = [folder['name'] for folder in folders]

# 폴더 추가 섹션
with st.expander("폴더 추가하기"):
    new_folder_name = st.text_input("새 폴더 이름:")
    add_folder_btn = st.button("폴더 추가")
    if add_folder_btn:
        response = api.create_folder(
            new_folder_name, st.session_state.username)
        if response.status_code == 204:
            st.success(f"'{new_folder_name}' 폴더가 추가되었습니다!")
            # 폴더 리스트 업데이트
            user = api.get_user_info(st.session_state.username)
            folders = user['folders']
            folder_names = [folder['name'] for folder in folders]
        elif response.status_code == 422:
            st.warning("폴더 이름을 입력해주세요.")
        elif response.status_code == 404:
            st.error("이미 존재하는 폴더 이름입니다.")

selected_folder_name = st.selectbox("폴더를 선택하세요:", folder_names)

# 선택한 폴더의 ID를 가져오기
selected_folder = next(
    folder for folder in folders if folder['name'] == selected_folder_name)
st.session_state['folder_id'] = selected_folder['id']

form = st.form(key="Create Note")
form.markdown("**새 노트 추가**")
topic = form.text_input("노트 제목:", value=st.session_state.get('note_title', ''))
content = form.text_area(
    "노트 내용:", value=st.session_state.get('note_content', ''), height=350)
submit = form.form_submit_button("노트 추가")

if submit:
    response = api.create_note(st.session_state['folder_id'], topic, content)
    if response.status_code == 204:
        st.success(f" '{topic}' 노트가 추가되었습니다!")
        if 'note_title' in st.session_state:
            st.session_state['note_title'] = ''
        if 'note_content' in st.session_state:
            st.session_state['note_content'] = ''
    elif response.status_code == 422:
        st.warning("모든 필드를 채워주세요.")
    elif response.status_code == 404:
        st.error("존재하지 않는 폴더입니다.")