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
    change_profile_picture
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
    change_profile_picture.bp
]
