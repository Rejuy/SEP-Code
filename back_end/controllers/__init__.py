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
    admin_operate_item,
    admin_edit_user,
    admin_get_single_user,
    admin_get_single_item,
    admin_edit_item,
    view_full_content,
    admin_get_online_time,
    get_random_list,
    new_user_count,
    admin_get_db_info,
    admin_get_comments,
    admin_get_single_comment,
    admin_edit_comment
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
    admin_operate_item.bp,
    admin_edit_user.bp,
    admin_get_single_user.bp,
    admin_get_single_item.bp,
    admin_edit_item.bp,
    view_full_content.bp,
    admin_get_online_time.bp,
    get_random_list.bp,
    new_user_count.bp,
    admin_get_db_info.bp,
    admin_get_comments.bp,
    admin_get_single_comment.bp,
    admin_edit_comment.bp
]
