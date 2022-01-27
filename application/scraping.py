import requests
from bs4 import BeautifulSoup

BASE_URL = "https://github.com/"


def fetch(since="weekly", language=''):
    res = requests.get(f"{BASE_URL}/trending{language}?since={since}")

    if res.status_code == 200:
        html_souce = res.text

        return html_souce, res.status_code
    else:
        return False, res.status_code


def scraping_repos(html_souce):
    soup = BeautifulSoup(html_souce, 'html.parser')
    repos = []

    for repo in soup.find_all('article', attrs={'class': 'Box-row'}):

        full_name = repo.h1.get_text().replace("\n", "").strip().replace(" ", "")

        author, repo_name = full_name.split('/')

        try:
            description = repo.p.get_text().strip()
        except:
            description = ''

        try:
            tag_div_with_stars = repo.find('div', attrs={'class': 'f6'})
            tag_a1, tag_a2 = tag_div_with_stars.find_all(
                'a', attrs={'class': 'Link--muted'})

            stars = tag_a1.get_text().strip().replace(',', '')
            forks = tag_a2.get_text().strip().replace(',', '')
        except:
            stars = 0
            forks = 0

        repo_obj = {
            "repo_name": repo_name,
            "full_name": full_name,
            "description": description,
            "stars": int(stars),
            "forks": int(forks),
            "author": author,
            "avatar_url": f"{BASE_URL}{author}.png",
            "repo_url": f"{BASE_URL}{full_name}"
        }

        repos.append(repo_obj)

    return repos


def get_trending(language):
    html_souce, status_code = fetch(language=language)

    if html_souce and status_code == 200:
        repos = scraping_repos(html_souce)
        return repos
    else:
        return False
