# 🌍 AI Language Translator Web App

A Flask-based web application that translates English text into Hindi using the **Helsinki-NLP/opus-mt-en-hi** transformer model from Hugging Face.

## 🚀 Features
- 🔤 English → Hindi translation
- 🤖 AI-powered using Hugging Face Transformers
- ⚡ Fast and simple web interface
- 🌐 Deployable on cloud platforms (Render)

## 🛠 Tech Stack
- Python
- Flask
- Hugging Face Transformers
- PyTorch
- HTML, CSS

## 📁 Project Structure
aitranslator-webapp/
│
├── app.py
├── templates/
│ └── index.html
├── docs/
│ ├── English_to_Hindi_Translator_SRS.pdf
│ └── language_translator_jira_backlog.xlsx
├── requirements.txt
├── .gitignore
└── README.md

## ⚙️ Installation & Setup

1. Clone the repository:
git clone https://github.com/fatimaaa013/aitranslator-webapp.git
cd aitranslator-webapp

2. Create virtual environment:
python -m venv venv
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
python app.py

5. Open in browser:
http://127.0.0.1:5000/

## 📌 Future Improvements
- Add multiple language support
- Improve UI/UX
- Add speech-to-text input
- Deploy using Docker
