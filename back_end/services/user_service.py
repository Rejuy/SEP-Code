from services.mysql_service import db
from headers import INT_TO_TABLE, INT_TO_BASIC_KEY_LIST
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

def getUserItems (user_id, class_id):
    try:
        table = INT_TO_TABLE[class_id]
        key_list = INT_TO_BASIC_KEY_LIST[class_id]
    except Exception as e:
        print("Error in <add_item_service.checkItemExisted>")
        print(e)
        return "error"
    return db.getData(table, ["user_id"], [user_id], key_list)[0]