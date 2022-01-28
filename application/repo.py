from flask import Blueprint, request, jsonify
from . import scraping

repo = Blueprint('repo', __name__)


@repo.route("/")
def get_trending():
    since = request.args.get('since') if request.args.get(
        'since') else 'daily'

    data = scraping.get_trending_repos('', since)

    if data:
        return jsonify(data), 200
    else:
        return 404


@repo.route("/<language>")
def get_language_trending(language):
    since = request.args.get('since') if request.args.get(
        'since') else 'daily'

    data = scraping.get_trending_repos(f"/{language}", since)

    if data:
        return jsonify(data), 200
    else:
        return 404
