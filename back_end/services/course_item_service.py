from headers import *
from services.mysql_service import db


def getCourseItem(id):
    item, flag = db.getItem("course_content", 1, id, ITEM_COURSE_KEY)
    return item, flag