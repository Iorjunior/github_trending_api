import imp
from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Sua_Chave_Secreta'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
