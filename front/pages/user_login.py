import streamlit as st

import api
import template

template.base()

if not st.session_state.auth:
    form = st.form(key="login")
    username = form.text_input("Username: ")
    password = form.text_input("Password: ", type="password")
    submit = form.form_submit_button("Log in")

    if submit:
        if not username:
            st.warning("You didn't fill out the username.")
        if not password:
            st.warning("You didn't fill out the password.")
        else:
            if username == st.secrets.user.username and password == st.secrets.user.password:
                st.success("You're Logged in!")
                st.session_state.auth = True

                st.session_state.username = username
                response = api.get_user_info(username)
                st.session_state.user_id = response['id']

                st.switch_page("index.py")
            else:
                st.error("Your username & password didn't match. Please try again.")
else:
    st.success("You've already logged in!")