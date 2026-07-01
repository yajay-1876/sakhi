import requests
import streamlit as st

# from frontend.services.assistant_response import assistant_response
from src.frontend.config.frontend_settings import Settings

settings = Settings()
BACKEND_URL = settings.BACKEND_URL


def create_conversation(user_query):
        try:
            user_id=st.session_state.user_id

            response = requests.post(
                f"{BACKEND_URL}/conversations/create",
                json={
                    "user_id"    : user_id,
                    "user_query" : user_query
                }
            )
            if response.status_code != 200:
                st.error(response.json()["detail"])
                return

            data = response.json()
            st.session_state.conversation_id  = data["conv_id"]

        except requests.exceptions.ConnectionError:
            st.error("Backend server is not running.")

        except Exception as e:
            st.error(str(e))