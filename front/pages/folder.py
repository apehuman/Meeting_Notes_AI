import streamlit as st
from datetime import datetime
import requests

import template

template.base()

if 'folder_id' not in st.session_state:
    st.switch_page("pages/folders.py")

# st.write(st.session_state)

folder_url = f"http://127.0.0.1:8000/folder/{st.session_state.folder_id}"
folder = requests.get(folder_url).json()

st.title(f"Folder: {folder['name']}")

st.header("Notes: ")
for note in folder['notes']:
    date_added = datetime.strptime(note['date_added'], "%Y-%m-%dT%H:%M:%S.%f")
    st.markdown(f"* {note['topic']} ({date_added.strftime("%Y-%m-%d %H:%M")})")
    st.markdown(f"&emsp;&emsp;{note['content']}")