from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

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

@app.route("/allrecipes")
def allrecipes():
    sql = "SELECT id, name, type FROM recipes"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return render_template("allrecipes.html", recipes=recipes)

@app.route("/newrecipe")
def newrecipe():
    return render_template("newrecipe.html")

@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    sql = "INSERT INTO recipes (name, type, cooktime, price, ingredient, instructions) VALUES (:name, type, cooktime, price, ingredient, instructions)"
    result = db.session.execute(sql, {"name":name})
    db.session.commit()
    return redirect("/allrecipes")

