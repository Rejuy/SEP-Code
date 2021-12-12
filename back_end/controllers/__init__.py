# -*- coding: utf-8 -*-

from controllers import (
    register_user,
    login,
    activate,
    feedback,
    save_images,
    comment,
    courses_list,
    course_item,
    user,
    places_list,
    place_item,
    foods_list,
    food_item,
    like,
    collection
)

blueprints = [
    register_user.bp,
    login.bp,
    activate.bp,
    feedback.bp,
    save_images.bp,
    courses_list.bp,
    comment.bp,
    course_item.bp,
    user.bp,
    places_list.bp,
    place_item.bp,
    foods_list.bp,
    food_item.bp,
    like.bp,
    collection.bp
]
