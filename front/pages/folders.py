import streamlit as st
import requests

import template


template.base()

folders_url = "http://127.0.0.1:8000/folder/list"
folders = requests.get(folders_url)

st.write("Folders")

if folders: 
    for folder in folders.json():
        if st.button(folder['name']):
            st.session_state.folder_id = folder['id']
            st.switch_page("pages/folder.py")
        # st.write(st.session_state)
else:
    st.write("No folders have been added yet")