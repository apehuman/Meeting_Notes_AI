import streamlit as st

def unauth_menu():
    st.sidebar.page_link("index.py", label="Sound Scanner", icon="🏠")
    st.sidebar.page_link("pages/user_login.py", label="Log in")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.page_link("index.py", label="Sound Scanner", icon="🏠")
    with col3:
        st.page_link("pages/user_login.py", label="Log in")

def auth_sidebar():
    st.sidebar.page_link("index.py", label="Sound Scanner", icon="🏠")
    st.sidebar.page_link("pages/folders.py", label="Folders", icon="📁")
    st.sidebar.page_link("pages/user_logout.py", label="Log out")

def base():
    """Parent Template"""
    # st.write(st.session_state)
    # init login session state
    if 'auth' not in st.session_state:
        st.session_state.auth = False
    
    if st.session_state.auth:
        auth_sidebar()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.page_link("index.py", label="Sound Scanner", icon="🏠")
        with col2:
            st.page_link("pages/folders.py", label="Folders", icon="📁")
        with col3:
            st.write(f"Hello, {st.session_state.username}")
            if st.button("Log out"):
                st.session_state.auth = False
                st.switch_page("pages/user_logout.py")
    else:
        unauth_menu()
    
    st.divider()