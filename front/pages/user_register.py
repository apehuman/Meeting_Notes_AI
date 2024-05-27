import streamlit as st

import api
import template

template.base()


form = st.form(key="Create User")
form.markdown("**Sign Up**")
username = form.text_input("Username: ")
passwd1 = form.text_input("Password: ", type="password")
passwd2 = form.text_input("Confirm Password: ", type="password")
submit = form.form_submit_button("Sign Up")

if submit:
    response = api.create_user(username, passwd1, passwd2)
    if (response.status_code == 204):
        st.success(f"User '{username}' has been signed up.")
        st.success("Congratulation! You've been signed up. Now you can log in!")
    elif (response.status_code == 422):
        st.warning("You should fill out the form.")
    elif (response.status_code == 409):
        st.error("이미 존재하는 사용자입니다.")