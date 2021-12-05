# -*- coding: utf-8 -*-

from controllers import (
    register_user,
    login,
    activate,
    feedback,
    save_images,
    courses_list,
    comment,
)

blueprints = [
    register_user.bp,
    login.bp,
    activate.bp,
    feedback.bp,
    save_images.bp,
    courses_list.bp,
    comment.bp
]
