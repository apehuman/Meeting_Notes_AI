import streamlit as st
import requests

import api
import template

template.base()

form = st.form(key="Create Folder")
folder_name = form.text_input("Add a new Folder: ", placeholder="Enter Folder name")
submit = form.form_submit_button("Add folder")

if submit:
    response = api.create_folder(folder_name)
    if(response.status_code == 204):
        st.success(f" '{folder_name}' has been added!")
    elif(response.status_code == 422):
        st.warning("You should enter any name.")
    elif(response.status_code == 404):
        st.error("Folder name already exsits")