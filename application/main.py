from flask import Blueprint, jsonify
from . import scraping

main = Blueprint('main', __name__)


@main.route("/")
def get_trending():
    data = scraping.get_trending('')

    if data:
        return jsonify(data), 200
    else:
        return 404


@main.route("/<language>")
def get_language_trending(language):
    data = scraping.get_trending(f"/{language}")

    if data:
        return jsonify(data), 200
    else:
        return 404
