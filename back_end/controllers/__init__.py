# -*- coding: utf-8 -*-

from controllers import (
    register_user,
    login,
    activate
)

blueprints = [
    register_user.bp,
    login.bp,
    activate.bp
]
