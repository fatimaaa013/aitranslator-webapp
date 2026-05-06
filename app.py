from flask import Flask, render_template, request, redirect, session
from transformers import MarianMTModel, MarianTokenizer
import json
import hashlib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")

# Ensure users.json exists
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump({}, f)

model_cache = {}
tokenizer_cache = {}

app = Flask(__name__)
app.secret_key = "your_secret_key"

# to select the model
model_name = "Helsinki-NLP/opus-mt-en-hi"
# to load the model
model = MarianMTModel.from_pretrained(model_name)
# to load the tokenizer
tokenizer = MarianTokenizer.from_pretrained(model_name)


# Translation function
def translate_text(text, src, tgt):
    model_name = f"Helsinki-NLP/opus-mt-{src}-{tgt}"

    try:
        if model_name not in model_cache:
            model_cache[model_name] = MarianMTModel.from_pretrained(model_name)
            tokenizer_cache[model_name] = MarianTokenizer.from_pretrained(model_name)

        model = model_cache[model_name]
        tokenizer = tokenizer_cache[model_name]

        inputs = tokenizer(text, return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        result = tokenizer.decode(translated[0], skip_special_tokens=True)

        return result

    except:
        return "Translation model not available for selected languages"


def translation(data, source_lang, target_lang):

    # Same language
    if source_lang == target_lang:
        return data

    # Step 1: ALWAYS convert source → English if needed
    if source_lang != "en":
        step1 = translate_text(data, source_lang, "en")
        if "not available" in step1:
            return "Source language not supported"
    else:
        step1 = data

    # Step 2: English → target
    if target_lang != "en":
        step2 = translate_text(step1, "en", target_lang)
        if "not available" in step2:
            return "Target language not supported"
        return step2

    return step1


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Translator page
@app.route("/translate", methods=["POST", "GET"])
def translate():
    if "user" not in session:
        return redirect("/login")
    translated_text = ""
    if request.method == "POST":
        data = request.form["data"]
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]

        translated_text = translation(data, source_lang, target_lang)

    return render_template("index.html", translated_text=translated_text)


@app.route("/")
def home():
    if "user" in session:
        return redirect("/translate")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect("/translate")

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            with open(USERS_FILE, "r") as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        if email in users and users[email]["password"] == hash_password(password):
            session["user"] = email
            return redirect("/translate")
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            with open(USERS_FILE, "r") as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        if email in users:
            return render_template("signup.html", error="User already exists")

        hashed_password = hash_password(password)
        users[email] = {"password": hashed_password}

        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)

        return redirect("/login")

    return render_template("signup.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


# For deployment

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    # Detect environment
    debug_mode = os.environ.get("ENV") != "production"

    app.run(host="0.0.0.0", port=port, debug=debug_mode)
