from app import app
from flask import redirect, render_template, request, session, abort
import users, recipes


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random",methods=["POST"])
def random():
    recipe = recipes.randomrecipe()
    return render_template("recipe.html",recipe=recipe)

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
    del session["user_id"]
    del session["csfr_token"]
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
    #if session["csfr_token"] != request.form["csfr_token"]:
        #return render_template("error.html", message="Something went wrong, could not post recipe.")
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

@app.route("/recipe/<int:id>")
def recipe(id):
    list = recipes.recipe(id)
    current_votes = recipes.count_votes(id)
    return render_template("recipe.html", recipe=list, current_votes=current_votes)

@app.route("/recipe/<int:id>/voting",methods=["GET", "POST"])
def voting(id):
    if request.method == "GET":
        return render_template("voting.html", id=id)
    if request.method == "POST":
        recipe_id = id
        vote = request.form["vote"]
        if recipes.voting(recipe_id,vote):
            list = recipes.recipe(recipe_id)
            current_votes = recipes.count_votes(recipe_id)
            return render_template("recipe.html", recipe=list, current_votes=current_votes)
        else:
            return render_template("error.html", message="Something went wrong, could not vote.")

@app.route("/test3")
def test3():
    return render_template("test3.html")