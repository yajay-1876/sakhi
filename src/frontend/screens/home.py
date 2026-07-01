import streamlit as st

from src.frontend.utils.take_user_query import take_user_query
from src.frontend.services.ask_answer import ask_answer
from src.frontend.services.create_conversation import create_conversation
from src.frontend.services.get_all_conversations import get_all_conversations
from src.frontend.utils.sidebar import render_sidebar
from src.frontend.services.upload_document import upload_document

def show_home_page():

    st.subheader("Sakhi💃")
    st.write(f"Welcome {st.session_state.username}")

    conversations = get_all_conversations()
    render_sidebar(conversations)

    has_conversation = st.session_state.conversation_id is not None

    # -----------------------------
    # Chat History
    # -----------------------------
    if has_conversation:
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])



    if has_conversation:

        uploaded_file = st.file_uploader(
            "Choose a PDF",
            type=["pdf"],
            key=f"upload_{st.session_state.conversation_id}"
        )

        if uploaded_file is not None:

            if st.button("Upload Document"):
                upload_document(st.session_state.conversation_id, uploaded_file)

    else:
        # -----------------------------
        # Upload Section
        # -----------------------------
        st.divider()
        st.subheader("📄 Upload PDF")
        st.info(
            "Create a conversation first. "
            "After the first message you can upload PDFs."
        )

    # -----------------------------
    # Chat Input
    # -----------------------------
    user_query = st.chat_input("Ask Sakhi...")

    if user_query:

        take_user_query(user_query)

        if not has_conversation:

            create_conversation(user_query)

        ask_answer(
            st.session_state.conversation_id,
            user_query
        )

        st.rerun()