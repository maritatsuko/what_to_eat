from app import app
from flask import redirect, render_template, request, session
import users, recipes


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Incorrect username or password")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")
        if users.register(username, password1):
            return redirect("/")
        else:
            render_template("error.html", message="Registration failed, please try again.")

@app.route("/newrecipe")
def newrecipe():
    return render_template("newrecipe.html")

@app.route("/allrecipes")
def allrecipes():
    list = recipes.get_recipes()
    return render_template("allrecipes.html", recipes=list)

@app.route("/create",methods=["POST"])
def create():
    name = request.form["name"]
    type = request.form["type"]
    cooktime = request.form["cooktime"]
    price = request.form["price"]
    ingredients = request.form.getlist("ingredient")
    instructions = request.form["instructions"]
    if recipes.create(name, type, cooktime, price, ingredients, instructions):
        return redirect("/allrecipes")
    else:
        return render_template("error.html", message="Something went wrong, could not post recipe.")

