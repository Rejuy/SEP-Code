import random
from services.mysql_service import db


def randomList():
    course_count = db.getTableCount("course_list")
    food_count = db.getTableCount("food_list")
    place_count = db.getTableCount("place_list")
    course_index = random.randint(0, course_count - 1)
    food_index = random.randint(0, food_count - 1)
    place_index = random.randint(0, place_count - 1)
    course_id, flag1 = db.randomItemId("course_list", course_index)
    if not flag1:
        return []
    food_id, flag2 = db.randomItemId("food_list", food_index)
    if not flag2:
        return []
    place_id, flag3 = db.randomItemId("place_list", place_index)
    if not flag3:
        return []
    return [
        {
            "type": 1,
            "id": course_id
        },
        {
            "type": 2,
            "id": food_id
        },
        {
            "type": 3,
            "id": place_id
        }
    ]

