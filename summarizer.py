import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def summarize_email(text: str) -> str:
    prompt = f"Summarize the following email or thread in bullet points with key takeaways:\n\n{text}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

