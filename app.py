import streamlit as st
import google.generativeai as genai
import os 
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt,image):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded") 
    
st.set_page_config(page_title="Healthy Reciepe WebApp")

st.header("Healthy Reciepe WebApp")
uploaded_file = st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me what healthy dish can I prepare with the ingredients which are present in the image ")

input_prompt="""
You are an expert in providing healthy dish receipe from all over the world. Analyse all the ingredients present in 
        the image and give me a healthy dish receipe that only requires those ingredients to prepare.

        1.Step by step reciepe.

    Finally also mention the carbs, protein,fiber,and fats present in per serving and also include serving size.


"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data)
    st.header("The Response is")
    st.write(response)