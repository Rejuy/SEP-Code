# -*- coding: utf-8 -*-

from controllers import (
    register_user,
    login,
    activate,
    feedback
)

blueprints = [
    register_user.bp,
    login.bp,
    activate.bp,
    feedback.bp
]
