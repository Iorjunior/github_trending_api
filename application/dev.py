from flask import Blueprint, request, jsonify
from .cache import cache
from . import scraping

dev = Blueprint('dev', __name__)


@dev.route("/", methods=['GET'])
@cache.cached(timeout=60*5)
def get_trending():
    since = request.args.get('since') if request.args.get(
        'since') else 'daily'

    data = scraping.get_treding_devs('', since)

    if data:
        return jsonify(data), 200
    else:
        return 404


@dev.route("/<language>", methods=['GET'])
@cache.cached(timeout=60*5)
def get_language_trending(language):
    since = request.args.get('since') if request.args.get(
        'since') else 'daily'

    data = scraping.get_treding_devs(f"/{language}", since)

    if data:
        return jsonify(data), 200
    else:
        return 404
