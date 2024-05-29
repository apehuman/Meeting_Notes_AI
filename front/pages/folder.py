import streamlit as st
from datetime import datetime
import template
import api

template.base()

# st.write(st.session_state)

if 'username' not in st.session_state:
    st.switch_page("pages/user_login.py")

else:
    if 'folder_id' not in st.session_state:
        st.session_state['folder_id'] = 1

folder = api.get_folder(st.session_state.folder_id)

# 사이드바에 노트 제목 목록 추가
st.sidebar.title("Notes List")
for note in folder['notes']:
    st.sidebar.write(note['topic'])


st.title(f":open_file_folder: Folder: {folder['name']}")

st.header("Notes: ")

st.page_link("pages/new_note_form.py", label="Add a new Note", icon="➕")

# CSS를 사용하여 노트 스타일 정의
st.markdown("""
    <style>
    .note-container {
        border-radius: 25px; /* 모서리를 동그랗게 */
        background: #f0f0f0; /* 배경색 */
        padding: 20px; /* 안쪽 여백 */
        margin: 10px 0; /* 위아래 마진 */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
    }
    </style>
    """, unsafe_allow_html=True)

notes = folder['notes']
for note in notes:
    date_added = datetime.strptime(note['date_added'], "%Y-%m-%dT%H:%M:%S.%f")
    date_added = date_added.strftime("%Y-%m-%d %H:%M")
    time = f"({date_added})"
    if note['date_edited']:
        date_edited = datetime.strptime(
            note['date_edited'], "%Y-%m-%dT%H:%M:%S.%f")
        date_edited = date_edited.strftime("%Y-%m-%d %H:%M")
        time += f" (last edited: {date_edited})"

    # 노트 컨테이너에 노트 내용을 HTML과 CSS로 스타일링하여 표시
    if len(note['content']) > 200:
        content = f"{note['content'][:200]}..."
    else:
        content = note['content']

    st.markdown(f"""
        <div class="note-container">
            <h4>* {note['topic']} {time}</h4>
            <p>&emsp;&emsp;{content}</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("Edit this note", key=note['id']):
        st.session_state.note_id = note['id']
        st.switch_page("pages/edit_note_form.py")
