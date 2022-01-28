from flask import Blueprint, request, jsonify
from . import scraping

dev = Blueprint('dev', __name__)


@dev.route("/", methods=['GET'])
def get_trending():
    since = request.args.get('since') if request.args.get(
        'since') else 'daily'

    data = scraping.get_treding_devs('', since)

    if data:
        return jsonify(data), 200
    else:
        return 404


@dev.route("/<language>", methods=['GET'])
def get_language_trending(language):
    since = request.args.get('since') if request.args.get(
        'since') else 'daily'

    data = scraping.get_treding_devs(f"/{language}", since)

    if data:
        return jsonify(data), 200
    else:
        return 404
