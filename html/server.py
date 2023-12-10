from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.post("/success-callback")
def show_main():
    return render_template('index.html')