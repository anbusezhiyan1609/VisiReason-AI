
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# 1. Load the .env file
load_dotenv() 

# 2. Setup the API Key
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    # If .env fails, this is a fallback for testing
    # Replace the string below with your actual key if .env still won't work
    genai.configure(api_key="your_api_key_here")

def get_gemini_repsonse(input_prompt, image_data, user_input):
    # This is the model that appeared in your list
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Send the prompt, the image, and the user's specific text
    response = model.generate_content([input_prompt, image_data[0], user_input])
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

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Gemini Health App")
st.header("Gemini Health App")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert nutritionist. Look at the food items in the image 
and calculate the total calories. Provide details of every food item 
with its calorie intake in the following format:

1. Item 1 - number of calories
2. Item 2 - number of calories
----
----
"""

if submit:
    if uploaded_file:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_repsonse(input_prompt, image_data, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload an image first!")