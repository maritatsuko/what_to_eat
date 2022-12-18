from db import db
import users

def get_recipes():
    sql = "SELECT id, name, type FROM recipes"
    result = db.session.execute(sql)
    return result.fetchall()

def create(name, type, cooktime, price, diet, description):
    creator = users.user_id()
    sql = "INSERT INTO recipes (creator, name, type, cooktime, price, description, diet) VALUES (:creator, :name, :type, :cooktime, :price, :description, :diet)"
    db.session.execute(sql, {"creator":creator, "name":name, "type":type, "cooktime":cooktime, "price":price, "description":description, "diet":diet})
    db.session.commit()
    return True

def recipe(id):
    sql = "SELECT * FROM recipes WHERE id=(:id)"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def creator_recipes(creator):
    sql = "SELECT id,name FROM recipes WHERE creator=(:creator)"
    result = db.session.execute(sql, {"creator":creator})
    return result.fetchall()

def mealtype_recipes(mealtype):
    sql = "SELECT id, name, type FROM recipes WHERE type=(:mealtype)"
    result = db.session.execute(sql, {"mealtype":mealtype})
    return result.fetchall()

def random_recipe():
    sql = "SELECT id FROM recipes ORDER BY RANDOM() LIMIT 1"
    result = db.session.execute(sql)
    if result is None:
        return 0
    return result.fetchone()[0]

def voting(recipe_id, vote):
    user_id = users.user_id()
    sql = "INSERT INTO votes (user_id, recipe_id, vote) VALUES (:user_id, :recipe_id, :vote)"
    db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id, "vote":vote})
    db.session.commit()
    return True

def count_votes(id):
    sql = "SELECT COUNT(recipe_id) FROM votes WHERE recipe_id=(:id)"
    result = db.session.execute(sql, {"id":id})
    if result is not None:
        sql = "SELECT SUM(vote) FROM votes WHERE recipe_id=(:id)"
        total = db.session.execute(sql, {"id":id})
        return total.fetchone()
    else:
        return 0
        