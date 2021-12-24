import random
from services.mysql_service import db
from headers import *


def randomList():
    course_count = db.getTableActivatedCount("course_list")
    food_count = db.getTableActivatedCount("food_list")
    place_count = db.getTableActivatedCount("place_list")
    course_index = random.randint(0, course_count - 1)
    food_index = random.randint(0, food_count - 1)
    place_index = random.randint(0, place_count - 1)
    course, flag1 = db.randomItemId("course_list", course_index, COURSES_KEY)
    if not flag1:
        return []
    food, flag2 = db.randomItemId("food_list", food_index, FOOD_KEY)
    if not flag2:
        return []
    place, flag3 = db.randomItemId("place_list", place_index, PLACE_KEY)
    if not flag3:
        return []
    course['department'] = course_scope_table[course['department']]
    course['type'] = course_type_table[course['type']]
    # course['schedule'] = course_schedule_table[course['schedule']]
    if food['scope'] == 1:
        food['type'] = inside_food_type_table[food['type']]
    else:
        food['type'] = outside_food_type_table[food['type']]
    food['scope'] = food_scope_table[food['scope']]
    place['type'] = place_type_table[place['type']]
    place['scope'] = place_scope_table[place['scope']]
    course['class'] = "课程"
    food['class'] = "餐饮"
    place['class'] = "地点"
    return [course, food, place]

