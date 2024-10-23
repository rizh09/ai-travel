# app.py
from flask import Flask, request, render_template
from openai import OpenAI
# Example in your Python code
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv('API_KEY')

client = OpenAI(api_key=APIKEY, base_url="https://api.chatanywhere.tech/v1")

app = Flask(__name__)

def gpt_35_api(messages: list):
    """Generate a response from ChatGPT for the provided messages."""
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return completion.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_question = request.form["question"]
        messages = [{'role': 'user', 'content': user_question}]
        response = gpt_35_api(messages)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)