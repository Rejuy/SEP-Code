import random
from services.mysql_service import db


def randomList():
    course_count = db.getTableCount("course_list")
    food_count = db.getTableCount("food_list")
    place_count = db.getTableCount("place_list")
    course_index = random.randint(0, course_count - 1)
    food_index = random.randint(0, food_count - 1)
    place_index = random.randint(0, place_count - 1)
    # course_id = db.getData("course_list", [], [], ["id"], get_all=)
    pass