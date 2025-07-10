import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_email(prompt: str) -> str:
    full_prompt = f"Write a professional email based on this request:\n\n{prompt}\n\nMake it clear and polite."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(full_prompt)
    return response.text.strip()

