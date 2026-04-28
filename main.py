from langchain_google_genai import chat_models, GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
import os
import streamlit as st
from dotenv import load_dotenv
model_1= langchain_google_genai(
    model="gemini-pro",
    temprature = 0,
    google_api_key=os.environ.get("GOOGLE_API_KEY")
)
load_dotenv()

st.header("Reserach-Tool")

user_input=st.text_input("PLease enter your research topic:")

if st.button("Summarize"):
    result = model_1.invoeke(user_input)
    st.write(result)