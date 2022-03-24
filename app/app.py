from flask import Flask
from . import simple_pages_outer


def create_app(): 
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask): 
    app.register_blueprint(simple_pages_outer.routes.blueprint)
