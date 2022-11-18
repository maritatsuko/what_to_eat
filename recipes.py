from db import db
import users

def get_recipes():
    sql = "SELECT id, name, type FROM recipes"
    result = db.session.execute(sql)
    return result.fetchall()

def create(name, type, cooktime, price, ingredients, instructions):
    creator = users.username()
    sql = "INSERT INTO recipes (creator, name, type, cooktime, price, ingredient, instructions) VALUES (:creator, :name, :type, :cooktime, :price, :ingredient, :instructions)"
    db.session.execute(sql, {"creator":creator, "name":name, "type":type, "cooktime":cooktime, "price":price, "ingredients":ingredients, "instructions":instructions})
    db.session.commit()
    return True
