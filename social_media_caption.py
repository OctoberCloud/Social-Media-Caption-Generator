import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Social Media Caption Generator")

desc = st.text_input("Product/Service Description")
tone = st.selectbox("Tone", ["Witty", "Professional", "Casual", "Inspirational"])

if st.button("Generate Captions"):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Write 3 social media captions under 30 words, tone: {tone}, about: {desc}"
    response = model.generate_content(prompt)
    st.write(response.text)