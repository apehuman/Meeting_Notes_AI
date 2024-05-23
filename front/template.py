import streamlit as st

def base():
    """Parent Template"""
    col1, col2 = st.columns(2)

    with col1:
        st.page_link("index.py", label="Sound Scanner", icon="🏠")
    with col2:
        st.page_link("pages/folders.py", label="Folders", icon="📁")
    st.divider()