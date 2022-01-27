from flask import Blueprint, jsonify, request
from . import scraping

main = Blueprint('main', __name__)


@main.route("/")
def get_trending():
    since = request.args.get('since') if request.args.get(
        'since') else 'daily'

    data = scraping.get_trending('', since)

    if data:
        return jsonify(data), 200
    else:
        return 404


@main.route("/<language>")
def get_language_trending(language):
    since = request.args.get('since') if request.args.get(
        'since') else 'daily'

    data = scraping.get_trending(f"/{language}", since)

    if data:
        return jsonify(data), 200
    else:
        return 404
