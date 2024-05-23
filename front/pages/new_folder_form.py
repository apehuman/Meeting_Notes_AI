import streamlit as st
import requests

import template

template.base()

form = st.form(key="Create Folder")
folder_name = form.text_input("Add a new Folder: ", placeholder="Enter Folder name")
submit = form.form_submit_button("Add folder")


folder_create_url = "http://127.0.0.1:8000/folder/create"

if submit:
    response = requests.post(folder_create_url, json={"name": folder_name})
    if(response.status_code == 204):
        st.success(f" '{folder_name}' has been added!")
    elif(response.status_code == 422):
        st.warning("You should enter any name.")
    elif(response.status_code == 404):
        st.error("Folder name already exsits")