import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.title("Grounded Knowledge Engine")

query = st.text_input("Enter your question:")

if st.button("Ask"):

    if query:

        try:
            response = requests.post(
                API_URL,
                json={"question": query}
            )

            if response.status_code == 200:

                result = response.json()

                st.subheader("Answer")

                st.text_area("Output", result.get("answer", ""), height=300)

            else:
                st.error("API request failed.")

        except Exception as e:
            st.error("Backend not running.")