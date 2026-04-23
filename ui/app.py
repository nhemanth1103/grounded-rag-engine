import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask-stream"

st.title("Grounded Knowledge Engine")
st.write("Ask questions from your document knowledge base.")

query = st.text_input("Enter your question:")

if st.button("Ask"):

    if query:

        response = requests.post(
            API_URL,
            json={"question": query}
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Answer")
            st.write(result["answer"])

        else:
            st.error("API request failed.")