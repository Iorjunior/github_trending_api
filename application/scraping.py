import requests
from bs4 import BeautifulSoup


BASE_URL = "https://github.com/"


def fetch(path, since='weekly', language=''):

    if path == 'repo':
        res = requests.get(
            f"{BASE_URL}/trending{language}?since={since}")

        if res.status_code == 200:
            html_souce = res.text

            return html_souce
        else:
            return False

    if path == 'dev':
        res = requests.get(
            f"{BASE_URL}/trending/developers{language}?since={since}")

        if res.status_code == 200:
            html_souce = res.text

            return html_souce
        else:
            return False


def scraping_repos(html_souce):
    soup = BeautifulSoup(html_souce, 'html.parser')
    repos = []

    for repo in soup.find_all('article', attrs={'class': 'Box-row'}):

        full_name = repo.h1.get_text().replace("\n", "").strip().replace(" ", "")

        author, repo_name = full_name.split('/')

        try:
            description = repo.p.get_text(strip=True)
        except:
            description = ''

        try:
            tag_div_with_stars = repo.find('div', attrs={'class': 'f6'})
            tag_a1, tag_a2 = tag_div_with_stars.find_all(
                'a', attrs={'class': 'Link--muted'})

            stars = tag_a1.get_text(strip=True).replace(',', '')
            forks = tag_a2.get_text(strip=True).replace(',', '')

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
            "avatar": f"{BASE_URL}{author}.png",
            "repo_url": f"{BASE_URL}{full_name}"
        }

        repos.append(repo_obj)

    return repos


def scraping_devs(html_souce):
    soup = BeautifulSoup(html_souce, 'html.parser')
    devs = []

    for dev in soup.find_all('article', attrs={'class': 'Box-row'}):

        rank_postion = dev.a.get_text(strip=True)
        dev_name = dev.h1.get_text(strip=True)

        try:
            username = dev.p.get_text(strip=True)
        except:
            username = dev_name

        try:
            tag_a_repo = dev.find_all('a', attrs={'class': 'css-truncate'})[0]
            repo_name = tag_a_repo.get_text(strip=True)
        except:
            repo_name = ''

        if repo_name:
            repo_url = f"{BASE_URL}{username}/{repo_name}"

            try:
                tag_div_description = dev.find_all(
                    'div', attrs={'class': 'f6'})[1]
                repo_description = tag_div_description.get_text(strip=True)
            except:
                repo_description = ''

        else:
            repo_description = ''
            repo_url = ''

        dev_obj = {
            "rank_position": int(rank_postion),
            "name": dev_name,
            "username": username,
            "dev_url": f"{BASE_URL}{username}",
            "avatar": f"{BASE_URL}{username}.png",
            "popularRepo": {
                "repo_name": repo_name,
                "description": repo_description,
                "url": repo_url
            }
        }

        devs.append(dev_obj)

    return devs


def get_trending_repos(language, since):
    html_souce = fetch('repo', language=language, since=since)

    if html_souce:
        repos = scraping_repos(html_souce)
        return repos
    else:
        return False


def get_treding_devs(language, since):
    html_souce = fetch('dev', language=language, since=since)

    if html_souce:
        repos = scraping_devs(html_souce)
        return repos
    else:
        return False
