import streamlit as st
import requests

from src.frontend.config.frontend_settings import Settings
settings=Settings()
BACKEND_URL=settings.BACKEND_URL

def login_user(username):
    try:
        response = requests.post(
            f"{BACKEND_URL}/auth/login",
            json={
                "username": username
            }
        )
        if response.status_code !=200:
            st.error(response.json()["detail"])
            return

        data = response.json()
        st.session_state.logged_in = True
        st.session_state.user_id   = data["user_id"]
        st.session_state.username  = data["username"]

        st.rerun()

    except requests.exceptions.ConnectionError:
        st.error("Backend server is not running.")

    except Exception as e:
        st.error(str(e))