import requests
import streamlit as st

from src.frontend.config.frontend_settings import Settings

settings = Settings()
BACKEND_URL = settings.BACKEND_URL


def get_chat_history():
    conv_id=st.session_state.conversation_id
    if conv_id:
        try:
            response = requests.post(
                f"{BACKEND_URL}/conversations/get_chat_history",
                json={
                    "conv_id"    : conv_id
                }
            )
            if response.status_code != 200:
                st.error(response.json()["detail"])
                return {}
            data = response.json()
            return data

        except requests.exceptions.ConnectionError:
            st.error("Backend server is not running.")
        except Exception as e:
            st.error(str(e))
    return {}