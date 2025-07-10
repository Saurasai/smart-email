import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def rewrite_email(text: str, tone: str) -> str:
    prompt = f"Rewrite the following email in a {tone} tone:\n\n{text}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

