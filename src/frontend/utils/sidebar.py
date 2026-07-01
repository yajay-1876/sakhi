import streamlit as st

from src.frontend.services.get_chat_history import get_chat_history

def render_sidebar(conversations: dict):
    with st.sidebar:
        st.write( st.session_state.username )
        st.header("🗨️ Chat History")

        if st.button("+ New Chat"):
            st.session_state.conversation_id = None
            st.session_state.chat_history = []
            st.rerun()

        # display all conversations in sidebar
        for cid, title in conversations.items():
            # Which conversation is currently open?
            is_current = cid == st.session_state.conversation_id  # cid == st.session_state.conversaion_id # return True if user on that chat doc
            if is_current:
                label = f"**{title}**"  # Current chat appears bold in sidebar
            else:
                label = title
            # Making every chat as a clickable button
            if st.button(label=label, key=f"conv_{cid}"):
                st.session_state.conversation_id = cid
                st.session_state.chat_history = get_chat_history()
