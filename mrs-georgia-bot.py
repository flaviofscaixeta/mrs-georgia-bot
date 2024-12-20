from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
import openai
from langdetect import detect

# Load environment variables from .env
dotenv_path = r'C:\Users\flavi\GitHub\Chatbot\.env'
load_dotenv(dotenv_path=dotenv_path)

# Verify if environment variables are loaded
required_env_vars = ["OPENAI_API_KEY", "TWILIO_SID", "TWILIO_AUTH_TOKEN"]
if all([os.getenv(var) for var in required_env_vars]):
    print("Environment variables loaded successfully.")
else:
    print("Error: Some environment variables are missing.")

# API Keys
openai.api_key = os.getenv("OPENAI_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = os.getenv("TWILIO_FROM_WHATSAPP")
TO_WHATSAPP = os.getenv("TWILIO_TO_WHATSAPP")

# Initialize the Twilio client
twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Configure Flask application
app = Flask(__name__)

# Function to generate ChatGPT response including lore
def generate_chatgpt_response(message):
    prompt = f"Please provide a courteous answer to the question: {message}"

    # AI Lore
    system_message = '''You are Mrs. Georgia, a friendly and experienced AI specializing in caring for plants, gardens, and weather.
    Provide cultivation tips, maintenance advice, and climate information. 
    If the question is outside your area of expertise, respond politely and indicate where more information can be found.
    Keep your tone clear, friendly, and concise.'''

    # Generate the response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

# Route to handle incoming messages via Twilio
@app.route("/sms", methods=["POST"])
def sms_reply():
    received_message = request.form.get("Body")
    sender_number = request.form.get("From")

    try:
        # Detect language
        detected_language = detect(received_message)
    except:
        detected_language = "unknown"

    if detected_language != "en":
        response_message = "Sorry, I can only respond to messages in English."
    elif not received_message or len(received_message.strip()) == 0:
        response_message = "Please send a valid message so I can assist you!"
    elif len(received_message) > 200:
        response_message = "Your message is too long! Please limit it to 200 characters."
    else:
        # Generate response if input is valid
        response_message = generate_chatgpt_response(received_message)

    # Send the response back via Twilio
    twilio_client.messages.create(
        body=response_message,
        from_=FROM_WHATSAPP,
        to=sender_number
    )
    return jsonify({'status': 'success'})

if __name__ == "__main__":
    app.run(debug=True)
