import streamlit as st
import requests

folder_list_url = "http://127.0.0.1:8000/folder/list"

folder_list = requests.get(folder_list_url)

if folder_list: 
    for folder in folder_list.json():
        st.markdown(f"* {folder['name']}")
else:
    st.write("No folders have been added yet")