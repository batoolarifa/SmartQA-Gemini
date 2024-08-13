
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# to load model and get response
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_reponse(input , image):



    if input !="":
        response = model.generate_content([input,image])
    else:
         response = model.generate_content(image)
    return response.text


st.set_page_config(page_title="Vision")
st.header(" Visual to Verbal Your Visual Storyteller")
input = st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an igmage...", type=["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)





submit = st.button("Tell me about the image")



if submit:
    response = get_gemini_reponse(input, image)
    st.subheader("The Response is")
    st.write(response)