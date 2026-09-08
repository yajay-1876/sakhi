import streamlit as st
from src.frontend.services.auth import login_user


def show_login_page():
    st.title("Sakhi💃")

    username = st.text_input(
        "Username",
        placeholder="Subbu@1611"
    )
    st.caption("Choose a unique username. You'll use the same username whenever you log in.")

    if st.button("Login"):
        if username and username.strip():
            login_user(username)
        else:
            st.warning("Please enter a username")
