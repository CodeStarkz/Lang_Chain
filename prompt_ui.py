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

paper_name = st.selectbox("Select a paper", ["Paper 1", "Paper 2", "Paper 3"])
style_input = st.selectbox(label="Select a style", options=["Super simplified", "Code and mathematical expression oriented"])
length_type = st.selectbox(label = "Select a length", options = ["Short", "Medium", "Long"])
if st.button("Summarize"):
    result = model_1.invoeke(user_input)
    st.write(result)

