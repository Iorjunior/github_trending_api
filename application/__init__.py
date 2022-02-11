from flask import Flask
from .cache import cache


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Sua_Chave_Secreta'

    cache.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .repo import repo as repo_blueprint
    app.register_blueprint(repo_blueprint, url_prefix='/repo')

    from .dev import dev as dev_blueprint
    app.register_blueprint(dev_blueprint, url_prefix='/dev')

    return app
