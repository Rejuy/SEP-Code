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
    admin_login,
    like,
    collection,
    search,
    user_count,
    user_list,
    add_item,
    admin_get_item_list,
<<<<<<< Updated upstream
    admin_operate_item
=======
    admin_operate_item,
    admin_edit_user,
    admin_get_single_user,
    admin_get_single_item,
    admin_edit_item
>>>>>>> Stashed changes
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
    admin_login.bp,
    like.bp,
    collection.bp,
    search.bp,
    user_count.bp,
    user_list.bp,
    add_item.bp,
    admin_get_item_list.bp,
<<<<<<< Updated upstream
    admin_operate_item.bp
=======
    admin_operate_item.bp,
    admin_edit_user.bp,
    admin_get_single_user.bp,
    admin_get_single_item.bp,
    admin_edit_item.bp
>>>>>>> Stashed changes
]
