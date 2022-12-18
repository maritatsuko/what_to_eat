from db import db

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
    sql = "SELECT DISTINCT favorites.recipe_id, recipes.name FROM favorites, recipes WHERE favorites.user_id=(:user_id) AND favorites.recipe_id = recipes.id"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()
    