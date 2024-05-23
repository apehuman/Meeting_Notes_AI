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

for note in folder['notes']:
    date_added = datetime.strptime(note['date_added'], "%Y-%m-%dT%H:%M:%S.%f")
    st.markdown(f"* {note['topic']} ({date_added.strftime("%Y-%m-%d %H:%M")})")
    st.markdown(f"&emsp;&emsp;{note['content']}")