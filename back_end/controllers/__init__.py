# -*- coding: utf-8 -*-

from controllers import (
    register_user,
    login,
    activate,
    feedback,
    save_images,
    courses_list,
    add_comment,
)

blueprints = [
    register_user.bp,
    login.bp,
    activate.bp,
    feedback.bp,
    save_images.bp,
    # viewfile.bp,
    courses_list.bp
]
