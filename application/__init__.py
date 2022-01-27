from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Sua_Chave_Secreta'

    return app
