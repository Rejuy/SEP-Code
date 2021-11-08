from flask import Flask
from controllers import blueprints


def createApp():
    app = Flask(__name__)

    # blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app

