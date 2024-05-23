import streamlit as st
import requests

import api
import template

template.base()

if 'folder_id' not in st.session_state:
    st.switch_page("pages/folders.py")

# st.write(st.session_state)
folder = api.get_folder(st.session_state.folder_id)
st.page_link("pages/folder.py", label=folder['name'], icon="📂")


if 'note_id' not in st.session_state:
    st.warning("You didn't choose any note!")
else:
    # if note has been chosen, prefill with info from the existing note
    note = api.get_note(st.session_state.note_id)

    form = st.form(key="Edit Note")
    form.markdown("**Edit Note**")
    topic = form.text_input("topic", note['topic'])
    content = form.text_area("content", note['content'])
    submit = form.form_submit_button("Save changes")

    if submit:
        if (topic == note['topic'] and content == note['content']):
            st.error("You didn't edit any words!")
        else: 
            response = api.update_note(note['id'], topic, content)
            if (response.status_code == 204):
                st.success(f" '{topic}' note has been edited!")
            elif (response.status_code == 422):
                st.warning("You should fill the form.")
            elif (response.status_code == 404):
                st.error("There's no such note")