from os import getenv
from flask import Flask
from flask import render_template, request

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/test", methods=["POST"]) #remove this later, testing form
def test():
    return render_template("test.html", name=request.form["name"])

@app.route("/register")
def register():
    return "Here you can register a new account."
