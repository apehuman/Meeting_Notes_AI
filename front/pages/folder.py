import streamlit as st
from datetime import datetime

import api
import template

template.base()

if 'folder_id' not in st.session_state:
    st.switch_page("pages/folders.py")

# st.write(st.session_state)

folder = api.get_folder(st.session_state.folder_id)

st.title(f":open_file_folder: Folder: {folder['name']}")

st.header("Notes: ")

st.page_link("pages/new_note_form.py", label="Add a new Note", icon="➕")

notes = folder['notes']
for note in notes:
    date_added = datetime.strptime(note['date_added'], "%Y-%m-%dT%H:%M:%S.%f")
    date_added = date_added.strftime("%Y-%m-%d %H:%M")
    time = f"({date_added})"
    if note['date_edited']:
        date_edited = datetime.strptime(note['date_edited'], "%Y-%m-%dT%H:%M:%S.%f")
        date_edited = date_edited.strftime("%Y-%m-%d %H:%M")
        time += f" (last edited: {date_edited})"

    st.markdown(f"* {note['topic']} {time}")

    st.markdown(f"&emsp;&emsp;{note['content']}")
    if st.button("Edit this note", key=note['id']):
        st.session_state.note_id = note['id']
        st.switch_page("pages/edit_note_form.py")