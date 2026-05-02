from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    response = client.responses.create(
        model="gpt-4o-mini",
        input=user_input
    )

    return jsonify({"reply": response.output_text})

if __name__ == "__main__":
    app.run(debug=True)