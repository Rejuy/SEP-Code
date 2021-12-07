from services.mysql_service import db

def updateProfilePicture (user_id, pic_url):
    db.updateData("user", "id", user_id, "image", pic_url)

def getProfilePicture (user_id):
    return db.getData("user", ["id"], [user_id], ["image"])[0][0]["image"]