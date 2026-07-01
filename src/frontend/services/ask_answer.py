import requests
import streamlit as st

from src.frontend.config.frontend_settings import Settings

settings = Settings()
BACKEND_URL = settings.BACKEND_URL


def ask_answer(conv_id, user_query):
    try:
        response = requests.post(
            f"{BACKEND_URL}/chat/ask",
            json={
                "conv_id"    : conv_id,
                "user_query" : user_query
            }
        )
        if response.status_code != 200:
            st.error(response.json()['detail'])
            return {}
        data = response.json()
        answer=data['answer']
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.chat_history.append({"role": "assistant", "content": answer})

    except requests.exceptions.ConnectionError:
        st.error("Backend server is not running.")
    except Exception as e:
        st.error(str(e))
    return {}


