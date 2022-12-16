from db import db
import users, recipes

def add_comment(recipe, comment):
    creator = users.user_id()
    sql = "INSERT INTO comments (creator, recipe, comment) VALUES (:creator, :recipe, :comment)"
    db.session.execute(sql, {"creator":creator, "recipe":recipe, "comment":comment})
    db.session.commit()
    return True

def get_comments(recipe):
    sql = "SELECT id, creator, comment FROM comments WHERE recipe=(:recipe) ORDER BY id"
    result = db.session.execute(sql, {"recipe":recipe})
    return result.fetchall()