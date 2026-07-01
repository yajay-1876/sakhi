import requests
import streamlit as st

from src.frontend.config.frontend_settings import Settings

settings = Settings()
BACKEND_URL = settings.BACKEND_URL


def upload_document(conv_id, uploaded_file):
        try:
            user_id=st.session_state.user_id

            response=requests.post(
                f"{BACKEND_URL}/document/upload",
                data={"conv_id": conv_id},
                files={
                    "uploaded_file":(
                        uploaded_file.name,
                        uploaded_file,
                        "application/pdf"
                    )
                }
            )
            if response.status_code != 200:
                st.error(response.json()["detail"])
                return {}

            data = response.json()

            if data['status']:
                st.success(f"{uploaded_file.name} upserted {data['chunks']} chunks successfully.")

            else:
                st.info(f"{uploaded_file.name} already provided in this chat.")

        except requests.exceptions.ConnectionError:
            st.error("Backend server is not running.")

        except Exception as e:
            st.error(str(e))