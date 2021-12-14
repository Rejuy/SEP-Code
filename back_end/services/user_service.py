from services.mysql_service import db

def updateProfilePicture (user_id, pic_url):
    db.updateData("user", "id", user_id, "image", pic_url)

def getProfilePicture (user_id):
    return db.getData("user", ["id"], [user_id], ["image"])[0][0]["image"]

def getUserInfo (user_id):
    return db.getData("user", ["id"],   [user_id], ["email", "like_count", "comment_count", "collection_count", "account_birth", "user_name"])[0][0]

def getUserFavorite (user_id):
    return db.getData("user_favorite", ["user_id"], [user_id], ["class", "item_id", "time", "item_name"])[0]

def getUserLike (user_name):
    like_list = db.getData("user_like", ["user"], [user_name], ["comment_id", "time"])[0]
    for i in range(len(like_list)):
        like_list[i]['comment'] = db.getData("comment", ["id"], [like_list[i]['comment_id']], ['class', 'item_id', 'user', 'text', 'image', 'star', 'time', 'likes'])[0]
    return like_list