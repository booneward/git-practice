import requests

URL = "https://api.github.com/users/octocat/repos"

def fetch_repos():
    resp = requests.get(URL, params={"per_page": 5}, timeout=10)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    for repo in fetch_repos():
        print(repo["name"], "-", repo["stargazers_count"], "stars")
