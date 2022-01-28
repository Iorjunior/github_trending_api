from flask import Blueprint, jsonify, request
from . import scraping

main = Blueprint('main', __name__)


@main.route("/")
def main_page():
    return '''
    <pre style="word-wrap: break-word; white-space: pre-wrap;">
    
    
    #Endpoints:
    
    /repo  
    /repo?since=weekly
    /repo/[language]

    /dev
    /dev?since=weekly
    /dev/[language]

    #Return Example: 
    
    /repo
    {
        "author": "public-apis",
        "avatar_url":   "https://github.com/public-apis.png",
        "description": "A collective list of free APIs",
        "forks": 20506,
        "full_name": "public-apis/public-apis",
        "repo_name": "public-apis",
        "repo_url": "https://github.com/public-apis/public-apis",
        "stars": 178065
    },
    ...
    
    /dev
    {
        "rank_position": 1,
            "name": PySimpleGUI,
            "username": PySimpleGUI,
            "dev_url": "https://github.com/PySimpleGUI",
            "avatar": "https://github.com/PySimpleGUI.png",
            "popularRepo": {
                "repo_name": "PySimpleGUI",
                "description": "Launched in 2018. It's 2022 and PySimpleGUI is actively developed & supported...",
                "url": "https://github.com/PySimpleGUI/PySimpleGUI"
            }
    },
    ...
    </pre>
    '''
