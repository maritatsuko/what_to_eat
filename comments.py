from db import db
import users

def add_comment(recipe, comment):
    creator = users.user_id()
    sql = "INSERT INTO comments (creator, recipe, comment) VALUES (:creator, :recipe, :comment)"
    db.session.execute(sql, {"creator":creator, "recipe":recipe, "comment":comment})
    db.session.commit()
    return True

def get_comments(recipe):
    sql = "SELECT comments.id, users.username, comments.comment FROM comments, users WHERE comments.recipe=(:recipe) AND comments.creator = users.id ORDER BY id DESC"
    result = db.session.execute(sql, {"recipe":recipe})
    return result.fetchall()