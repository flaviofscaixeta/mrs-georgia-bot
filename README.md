# Mrs. Georgia Bot 🌱  
Mrs. Georgia is a friendly AI assistant specializing in plant care and gardening. She offers tips on cultivation, maintenance, and general seasonal advice, always responding politely and helpfully.

## Features  
-### Features
- 🌿 **Cultivation Tips**: Learn how to care for your plants, including watering, sunlight needs, and soil tips.
- ☀️ **Weather-Related Suggestions**: Provides general advice based on user inputs about weather or seasonal changes.
- 🔔 **WhatsApp Integration**: Chat directly with Mrs. Georgia using Twilio.

## Project Structure  
```
miss_georgia_bot/  
├── app.py                  # Main application code  
├── requirements.txt        # Project dependencies  
├── .env.example            # Example environment variables file  
├── README.md               # Project documentation  
└── .gitignore              # Files ignored by Git  
```  

## Prerequisites  
- Python 3.8 or higher  
- OpenAI account (API Key)  
- Twilio account (SID and Auth Token)  

## Installation  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/your-username/miss_georgia_bot.git  
   cd miss_georgia_bot  
   ```  

2. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Configure the `.env` File**:  
   Create a `.env` file in the project's root directory with the following environment variables:  
   ```plaintext  
   OPENAI_API_KEY=your_openai_api_key  
   TWILIO_SID=your_twilio_sid  
   TWILIO_AUTH_TOKEN=your_twilio_auth_token  
   TWILIO_FROM_WHATSAPP=+your_twilio_number  
   TWILIO_TO_WHATSAPP=+user_number  
   ```  

## How to Run  
1. Start the Flask server:  
   ```bash  
   python app.py  
   ```  
2. The application will be available locally at:  
   ```bash  
   http://127.0.0.1:5000  
   ```  
3. Test it by sending messages via Twilio WhatsApp to interact with Mrs. Georgia.  

## Endpoints  
- **/sms**: Receives messages via Twilio and responds using Mrs. Georgia's AI.  
   - **Method**: POST  
   - **Parameters**:  
     - `Body` (text): Message sent by the user.  
     - `From` (string): Sender's phone number.  

## Example of Functionality  
1. User sends the message: "How do I take care of lettuce?"  
2. Mrs. Georgia responds: "To grow lettuce, keep the soil moist, ensure good drainage, and provide indirect light for at least 6 hours a day. Avoid extreme temperatures and fertilize moderately."  

## Contribution  
1. Fork the project.  
2. Create a branch for your new feature:  
   ```bash  
   git checkout -b my-new-feature  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Added new feature X"  
   ```  
4. Push the changes:  
   ```bash  
   git push origin my-new-feature  
   ```  
5. Open a Pull Request!  

## License  
This project is licensed under the MIT License.  

---  
Ready! 🌱🚀  
Mrs. Georgia is here to help you take care of your plants with all the care and efficiency. 🌿
