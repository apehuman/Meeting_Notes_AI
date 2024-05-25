import streamlit as st

import api
import template


template.base()

st.write("Folders")

st.page_link("pages/new_folder_form.py", label="Add a new Folder", icon="➕")

# folders = api.get_folders()
user = api.get_user_info(st.session_state.username)
folders = user['folders']

if folders: 
    for folder in folders:
        if st.button(folder['name']):
            st.session_state.folder_id = folder['id']
            st.switch_page("pages/folder.py")
        # st.write(st.session_state)
else:
    st.write("No folders have been added yet")