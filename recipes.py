from db import db
import users

def get_recipes():
    sql = "SELECT id, name, type FROM recipes"
    result = db.session.execute(sql)
    return result.fetchall()

def create(name, type, cooktime, price, ingredient, instructions):
    creator = users.user_id()
    sql = "INSERT INTO recipes (creator, name, type, cooktime, price, ingredient, instructions) VALUES (:creator, :name, :type, :cooktime, :price, :ingredient, :instructions)"
    db.session.execute(sql, {"creator":creator, "name":name, "type":type, "cooktime":cooktime, "price":price, "ingredient":ingredient, "instructions":instructions})
    db.session.commit()
    return True

def recipe(id):
    sql = "SELECT * FROM recipes WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def randomrecipe():
    sql = "SELECT id FROM recipes ORDER BY RANDOM() LIMIT 1"
    result = db.session.execute(sql)
    if result is None:
        return 0
    return result.fetchone()