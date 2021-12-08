from services.mysql_service import db

def getNameByID (user_id):
    return db.getData("user", ["id"], [user_id], ["user_name"])[0][0]["user_name"]