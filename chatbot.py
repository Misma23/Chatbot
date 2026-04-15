from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from groq import Groq
import sqlite3
import re
app = Flask(__name__)
app.secret_key = "secret123"
app.config['SESSION_TYPE'] = 'filesystem'
client = Groq(api_key="YOUR_KEY")
chat_history = []
# ---------------- DATABASE ----------------
def get_db():
    return sqlite3.connect("users.db")
def create_table():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

create_table()
# ---------------- HOME ----------------
@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("chat"))
    return render_template("welcome.html")
# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("chat"))
        else:
            return render_template("login.html", error="Invalid username or password ❌")
    return render_template("login.html")
# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 🔐 PASSWORD VALIDATION
        if len(password) < 6:
            return render_template("register.html", error="Password must be at least 6 characters")

        if not re.search("[A-Z]", password):
            return render_template("register.html", error="Must include 1 uppercase letter")

        if not re.search("[0-9]", password):
            return render_template("register.html", error="Must include 1 number")

        conn = get_db()
        cur = conn.cursor()

        try:
            cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
            conn.commit()
        except:
            conn.close()
            return render_template("register.html", error="Username already exists ❌")

        conn.close()
        return redirect(url_for("login"))

    return render_template("register.html")

# ---------------- CHAT PAGE ----------------
@app.route("/chat")
def chat():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------------- CHATBOT API ----------------
@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.json.get("message", "")

    if not user_input:
        return jsonify({"reply": "Please type something 🤔"})

    chat_history.append({"role": "user", "content": user_input})

    try:
        chat_completion = client.chat.completions.create(
            messages=chat_history,
            model="llama-3.1-8b-instant"
        )

        reply = chat_completion.choices[0].message.content
        chat_history.append({"role": "assistant", "content": reply})

    except Exception:
        reply = "⚠️ Server busy, try again later"

    return jsonify({"reply": reply})

# ---------------- CLEAR CHAT ----------------
@app.route("/clear", methods=["POST"])
def clear_chat():
    global chat_history
    chat_history = []
    return jsonify({"status": "cleared"})

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)