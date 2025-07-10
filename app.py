import streamlit as st
from utils.generator import generate_email
from utils.summarizer import summarize_email
from utils.rewriter import rewrite_email
from components.ui import tone_options

st.title("📧 Smart Email Assistant (Powered by Gemini)")
st.subheader("Use AI to generate, summarize, or rewrite your emails")

option = st.selectbox("Choose a task:", ["Generate Email", "Summarize Email", "Rewrite Email"])

if option == "Generate Email":
    prompt = st.text_area("What should the email say? (e.g., 'write a follow-up after interview')")
    if st.button("Generate"):
        with st.spinner("Generating..."):
            result = generate_email(prompt)
            st.text_area("Generated Email:", result, height=300)

elif option == "Summarize Email":
    input_text = st.text_area("Paste the full email or thread:")
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            result = summarize_email(input_text)
            st.text_area("Summary:", result, height=200)

elif option == "Rewrite Email":
    email_text = st.text_area("Paste the email to rewrite:")
    tone = st.selectbox("Select tone:", tone_options())
    if st.button("Rewrite"):
        with st.spinner("Rewriting..."):
            result = rewrite_email(email_text, tone)
            st.text_area("Rewritten Email:", result, height=300)

