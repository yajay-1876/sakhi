from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
st.set_page_config(
    page_title="Sakhi",
    page_icon="💃",
    layout="centered",
    initial_sidebar_state="collapsed"
)

from src.frontend.screens.login import show_login_page
from src.frontend.screens.home import show_home_page

# Session State default values
st.session_state.setdefault("user_id", None)
st.session_state.setdefault("username", None)
st.session_state.setdefault("logged_in",None)
st.session_state.setdefault("conversation_id", None)
st.session_state.setdefault("conversation_title", None)
st.session_state.setdefault("chat_history", [])    # [{role, content},{role, content}]

if st.session_state.logged_in:
    show_home_page()
else:
    show_login_page()