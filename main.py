"""
Install the Google AI Python SDK

$ pip install google-generativeai

"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from PIL import Image  # Import the Pillow library correctly


load_dotenv()  # Load environment variables from .env


# Configure the API key
my_api_key = os.getenv("API_KEY")
genai.configure(api_key = my_api_key)

# Create the model
generation_config = {
    "temperature": 0.4,
    "top_p": 1.0,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

# Define safety settings - Adjust these as needed

# safety_settings = {
#     HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
#     HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
#     # Add more categories as needed
# }

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    #safety_settings=safety_settings
)

chat_session = model.start_chat(history=[])

# ... (rest of your chat logic)
def chat_with_gemini():
    print("Chat with Gemini. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            break

        if user_input.startswith("img:"):
            # Assuming img: is the prefix for image inputs
            image_path = user_input.split("img:")[1].strip()
            try:
                # Open the image using Pillow
                image = Image.open(image_path)
                # Send the image to the API
                response = chat_session.send_message(image)
                print("Gemini: " + response.text)
            except FileNotFoundError:
                print(f"Error: Image file not found at '{image_path}'")
            except Exception as e:
                print(f"Error loading image: {e}")
        else:
            response = chat_session.send_message(user_input)
            print("Gemini: " + response.text)

if __name__ == "__main__":
    chat_with_gemini()