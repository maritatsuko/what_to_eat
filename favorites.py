from db import db
import users, recipes

def add_favorite(user_id, recipe_id):
    sql = "INSERT INTO favorites (user_id, recipe_id, favorite) VALUES (:user_id, :recipe_id, :favorite)"
    db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id, "favorite":True})
    db.session.commit()
    return True

def is_favorite(user_id, recipe_id):
    sql = "SELECT favorite FROM favorites WHERE user_id=(user_id) AND recipe_id=(recipe_id)"
    result = db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id})
    if result is False:
        return False
    return True

def user_favorites(user_id):
    sql = "SELECT recipe_id FROM favorites WHERE user_id=(:user_id)"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()