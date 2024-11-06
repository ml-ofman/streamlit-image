from dotenv import load_dotenv
load_dotenv() # Load all the environment variable from .env


import streamlit as st
import os 
from PIL import Image
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Version

model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text


def input_image_details(upload_file):
    if upload_file is not None:
        # Read the file into bytes
        bytes_data = upload_file.getvalue()

        image_parts = [
            {
                "mime_type": upload_file.type, # get the mime type the 
                "data": bytes_data 
            }
        ]
        return image_parts
    else:
        raise FileExistsError("No file uploaded")
 



# initilize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt : ", key="input")
upload_file = st.file_upload("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])
image=""
if upload_file is not None:
    image=image.open(upload_file)
    st.image(image, cation="Upload Image. ", use_column_width=True)



submit = st.button("Tell me about the invoice")

input_prompt="""
You are an expert in understanding invoices. We will upload a image as invoice
and you will have to answer any questions based on the uploaded invoice image
"""

# if submit button is clicked
if submit: 
    image_data = input_image_details(upload_file)
    response=get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is ")
    st.write(response)

 



























