from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

headers = {
    "authorization":st.secrets['GOOGLE_API_KEY'],
    "content-type": "application/json",
 }


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# to load model and get response
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_reponse(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q/A App")
st.header("Q/A  LLM Application")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")



if submit:
    response = get_gemini_reponse(input)
    st.subheader("The Response is")
    st.write(response)