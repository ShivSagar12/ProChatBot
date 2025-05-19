"# ProChatBot" 
 AI Chatbot using Cohere API and Flask
 =====================================
 This project is a simple AI chatbot web application that mimics GPT-like conversational responses
 using the Cohere API. 
It leverages Python, Flask for the backend, and WTForms for form handling. The app allows users
 to input questions and 
receive intelligent, conversational responses powered by the latest Cohere language model.
 Features--------- Natural conversation with Cohere's `command-nightly` model.- Clean and responsive web interface built with HTML and CSS.- Flask-powered backend with WTForms integration.- Easy to run locally in a virtual environment.
 Tech Stack----------- Python 3.x- Flask- Flask-WTF- Cohere API- HTML/CSS
 Prerequisites
------------
Cohere Chatbot Project - README
 Ensure you have the following installed:- Python 3.x- pip (Python package installer)
 Installation-----------
1. Clone the Repository
    git clone https://github.com/your-username/cohere-chatbot.git
    cd cohere-chatbot
 2. Create and Activate a Virtual Environment
    python -m venv chatbot
    chatbot\Scripts\activate   # For Windows
    source chatbot/bin/activate  # For Mac/Linux
 3. Install Dependencies
    pip install -r requirements.txt
    If `requirements.txt` is not available, manually install:
    pip install flask flask-wtf cohere
Cohere Chatbot Project - README
 4. Add Your Cohere API Key
 Replace 'YOUR_API_KEY' in `app.py` with your actual Cohere API key.
 How it Works------------- User inputs a question.- The question is sent to Cohere?s `command-nightly` model using the `chat()` endpoint.- The response is returned and displayed on the same webpage.
 Project Structure----------------
cohere-chatbot/
 ?
 ??? templates/
 ?   ??? home.html          # HTML template for UI
 ?
 ??? app.py                 # Main Flask app
 ??? README.md              # Project documentation
 ??? requirements.txt       # Python dependencies
 Usage----
To run the app:
    python app.py
Cohere Chatbot Project - README
 Then open your browser and go to:
    http://127.0.0.1:5000/
 UI Preview---------
A simple web UI with a text box and submit button:- Input: "What is Cohere?"- Output: AI-generated response from Cohere API
 Example Output-------------
User: What is Cohere?
 Bot: Cohere is a platform that provides large language models for developers to build natural
 language understanding applications...
 License------
This project is licensed under the MIT License. See the LICENSE file for more details.
 Acknowledgements----------------- Cohere ? for their powerful language models and APIs.- Flask ? for the lightweight Python web framework
