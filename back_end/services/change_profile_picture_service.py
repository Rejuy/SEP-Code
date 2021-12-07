from services.mysql_service import db

def updateProfilePicture (user_name, pic_url):
    db.updateData("user", "user_name", user_name, "image", pic_url)