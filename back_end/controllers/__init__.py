# -*- coding: utf-8 -*-

from controllers import (
    register_user,
    login,
    activate,
    feedback,
    save_images,
    # viewfile,
    courses_list,
    course_item
)

blueprints = [
    register_user.bp,
    login.bp,
    activate.bp,
    feedback.bp,
    save_images.bp,
    # viewfile.bp,
    courses_list.bp,
    course_item.bp
]
