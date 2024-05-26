import streamlit as st

import template

template.base()

# st.write(st.session_state)
if st.session_state.auth: 
    st.success("You're logged in now!")
else:
    st.markdown("#### You've been logged out. Thank you for visiting!")
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]