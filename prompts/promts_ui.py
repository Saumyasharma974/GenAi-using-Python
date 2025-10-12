from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os

# Load API key from .env
load_dotenv()

st.title("🧠 Research Assistant - Google GenAI")

# Get user input
user_input = st.text_input("Enter your query:")

# Button to submit query
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a query.")
    else:
        try:
            # Initialize chat model
            chat = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",  # or gemini-1.5-pro
                temperature=0.7,
                api_key=os.getenv("GOOGLE_API_KEY")
            )

            # Get response
            response = chat.invoke(user_input)
            st.success("Response:")
            st.write(response.content if hasattr(response, "content") else response)

        except Exception as e:
            st.error(f"Error: {e}")
