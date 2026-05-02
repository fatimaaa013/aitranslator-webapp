# 🌍 AI Language Translator Web App

A Flask-based web application that supports multi-language translation using Hugging Face transformer models, along with user authentication and an interactive UI.

---

## 🚀 Features
- 🌐 Multi-language translation (English, Hindi, French, Spanish, German)
- 🔐 User authentication (Login & Signup)
- 🔄 Language selection and swapping
- 📋 Copy translated text
- ⚡ Clean and responsive UI
- 🌐 Deployable on cloud platforms (Hugging Face Spaces using Flask)

---

## 🛠 Tech Stack
- Python
- Flask
- Hugging Face Transformers
- PyTorch
- HTML, CSS

---

## 📁 Project Structure
```bash
aitranslator-webapp/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/fatimaaa013/aitranslator-webapp.git
cd aitranslator-webapp
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python app.py
```

5. Open in browser:
```bash
http://127.0.0.1:5000/
```

---

## 📌 Future Improvements
- Add regional language support
- Improve translation accuracy with better models
- Add speech-to-text input
- Add translation history
- Deploy using Docker for scalability