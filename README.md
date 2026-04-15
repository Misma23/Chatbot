# 🤖 AI Chatbot Web App (Flask + Groq)

## 📌 Overview

This is a simple **AI Chatbot Web Application** built using **Flask**, **SQLite**, and **Groq API**.
It includes user authentication (Login/Register), password validation, and a chatbot interface.

---

## 🚀 Features

* 🔐 User Registration & Login
* ✅ Password validation (uppercase + number + length)
* 💬 AI Chatbot using Groq API
* 🧹 Clear chat option
* 🔓 Logout functionality
* 🎨 Styled UI with animations

---

## 📁 Project Structure

```
Chatbot/
│
├── chatbot.py
├── users.db
├── templates/
│     ├── welcome.html
│     ├── login.html
│     ├── register.html
│     ├── index.html
├── build/        (optional)
├── dist/         (optional)
└── chatbot.spec  (optional)
```

---

## ⚙️ Installation

### 1️⃣ Clone or Download

```
git clone <your-repo-link>
cd Chatbot
```

### 2️⃣ Install Dependencies

```
pip install flask groq pyinstaller
```

---

## 🔑 Setup API Key

Open `chatbot.py` and replace:

```python
client = Groq(api_key="YOUR_API_KEY_HERE")
```

---

## ▶️ Run the App

```
python chatbot.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🔐 Password Rules

* Minimum 6 characters
* At least 1 uppercase letter
* At least 1 number

Example:

```
Test123 ✅
```

---

## 🛠️ Build EXE File (Optional)

```
python -m PyInstaller --onefile --add-data "templates;templates" chatbot.py
```

Output:

```
dist/chatbot.exe
```

---

## ⚠️ Important Notes

* Do NOT open HTML files directly
* Always use Flask server
* Restart server after changes
* Use Incognito if UI not updating

---


## 💡 Future Improvements

* Chat history per user
* Better UI (like ChatGPT)
* Password hashing (security)
* Database upgrade (MySQL)

---


## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
