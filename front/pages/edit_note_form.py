import streamlit as st

import ai_text
import api
import template

template.base()

if 'folder_id' not in st.session_state:
    st.switch_page("pages/folders.py")

# st.write(st.session_state)
folder = api.get_folder(st.session_state.folder_id)
st.page_link("pages/folder.py", label=folder['name'], icon="📂")
###############################################################################

def make_containers(meeting_summary):
    """Make 3 sections of meeting summary"""
    container1 = st.container(border=True)
    container1.write(meeting_summary[0])
    container2 = st.container(border=True)
    container2.write(meeting_summary[1])
    container3 = st.container(border=True)
    container3.write(meeting_summary[2])

###############################################################################
# chat: 발화자 구분
@st.experimental_fragment
def speaker_recognition(content):
    if content[0:3] != "발화자":
        st.warning("발화자 구분 회의록 형식이 아닙니다.")
    else: 
        lines = content.splitlines()
        for line in lines:
            with st.chat_message(line[4]):
                st.markdown(line[8:])
###############################################################################

if 'note_id' not in st.session_state:
    st.warning("You didn't choose any note!")
else:
    # if note has been chosen, prefill with info from the existing note
    note = api.get_note(st.session_state.note_id)

    form = st.form(key="Edit Note")
    form.markdown("**Edit Note**")
    topic = form.text_input("topic", note['topic'])
    content = form.text_area("content", note['content'], height=400)
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


    with st.expander("**요약**"):
        if note['summary']:
            st.markdown(note['summary'])
            st.divider()
        ai_text.summary_3lines(note['id'], note['content'])

    with st.expander("**회의록 요약**"):
        if note['meeting_summary']:
            meeting_summary = note['meeting_summary']
            meeting_summary = meeting_summary.split('\n\n')
            make_containers(meeting_summary)
            st.divider()
        ai_text.summary_meeting(note['id'], note['content'])
    
    with st.expander("**번역**"):
        if note['translation']:
            st.markdown(note['translation'])
            st.divider()
        ai_text.translate(note['id'], note['content'])
    
    with st.expander("**발화자 구분**"):
        if st.button("발화자 구분", key="화자 구분"): 
            speaker_recognition(note['content'])