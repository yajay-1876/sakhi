import streamlit as st

from frontend.utils.take_user_query import take_user_query
from src.frontend.services.ask_answer import ask_answer
from src.frontend.services.create_conversation import create_conversation
from src.frontend.utils.sidebar import render_sidebar
from src.frontend.services.get_all_conversations import get_all_conversations

def show_home_page():

    st.subheader("Sakhi💃")
    st.write(f"Welcome {st.session_state.username}")
    conversations = get_all_conversations()
    render_sidebar(conversations)

    if st.session_state.conversation_id is None:
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
        if uploaded_file:
            st.write("Please start a conversation to upload files.")
        user_query = st.chat_input("Ask Sakhi...")
        if user_query:
            take_user_query(user_query)
            create_conversation(user_query)
            ask_answer(st.session_state.conversation_id, user_query)
            st.write("Inside create conversation")
            st.rerun()

    if st.session_state.conversation_id:
        st.write("Old conversation")
        # Show Chat History
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
        if uploaded_file:
            st.write("Uploading file in old conversation")
            pass
        user_query = st.chat_input("Ask Sakhi...")
        if user_query:
            st.write("second user_query")
            take_user_query(user_query)
            ask_answer(st.session_state.conversation_id, user_query)
