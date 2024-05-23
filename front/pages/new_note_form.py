import streamlit as st

import api
import template


template.base()

if 'folder_id' not in st.session_state:
    st.switch_page("pages/folders.py")

# st.write(st.session_state)
folder = api.get_folder(st.session_state.folder_id)
st.page_link("pages/folder.py", label=folder['name'], icon="📂")


form = st.form(key="Create Note")
form.markdown("**Add a new Note**")
topic = form.text_input("Add a new topic: ")
content = form.text_area("Add a new content: ")
submit = form.form_submit_button("Add Note")

if submit:
    response = api.create_note(folder['id'], topic, content)
    if(response.status_code == 204):
        st.success(f" '{topic}' note has been added!")
    elif(response.status_code == 422):
        st.warning("You should fill the form.")
    elif(response.status_code == 404):
        st.error("There's no such folder")