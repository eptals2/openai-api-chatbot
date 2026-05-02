# 🤖 Flask Chatbot using OpenAI API

A simple web-based chatbot built with Flask and the OpenAI API.
This project demonstrates how to connect a Python backend to an AI model and interact through a basic web interface.

---

## 🚀 Features

* 🧠 AI-powered chatbot (OpenAI API)
* 🌐 Flask backend
* 💬 Simple chat interface (HTML + JavaScript)
* 🔐 Secure API key handling using `.env`
* ⚡ Real-time responses

---

## 📁 Project Structure

```
openai-chatbot/
│── app.py
│── .env
│── requirements.txt
│── templates/
│     └── index.html
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/openai-chatbot.git
cd openai-chatbot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

Or manually:

```
pip install flask openai python-dotenv
```

---

## 🔑 Setup API Key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ **Important:**

* Do NOT share your API key publicly
* Add `.env` to `.gitignore`

---

## ▶️ Run the App

```
python app.py
```

Then open your browser:

```
http://127.0.0.1:5000
```

---

## 💡 Usage

1. Type a message in the input box
2. Click **Send**
3. The chatbot will respond instantly

---

## ❗ Troubleshooting

### Error: `429 insufficient_quota`

* Check your billing at OpenAI dashboard
* Ensure you have available credits

### API Key not working

* Make sure `.env` is loaded correctly
* Restart the app after changes

---

## 🛠️ Tech Stack

* Python
* Flask
* OpenAI API
* HTML, CSS, JavaScript

---

## 📌 Future Improvements

* Chat history (memory)
* Better UI (Bootstrap 5)
* User authentication
* Deployment (Render / Railway)
* Integration with NLP systems (e.g., resume screening)

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

Ephraim Talaba
Computer Science Student

---

## ⭐ Acknowledgements

* OpenAI for providing the API
* Flask community
