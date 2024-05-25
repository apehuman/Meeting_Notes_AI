import streamlit as st

def base():
    """Parent Template"""
    col1, col2, col3 = st.columns(3)

    with col1:
        st.page_link("index.py", label="Sound Scanner", icon="🏠")
    with col2:
        st.page_link("pages/folders.py", label="Folders", icon="📁")
    with col3:
        # init login session state
        if 'auth' not in st.session_state:
            st.session_state.auth = False
        
        if st.session_state.auth:
            st.write(f"Hello, {st.session_state.username}")
            if st.button("Log out"):
                st.session_state.auth = False
                st.switch_page("pages/user_logout.py")
        else:
            st.page_link("pages/user_login.py", label="Log in")
    st.divider()