import sys
import requests

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    try:
        resp = requests.get(url, params={"per_page": 5}, timeout=10)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []
    return resp.json()

if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) > 1 else "octocat"
    for repo in fetch_repos(username):
        print(repo["name"], "-", repo["stargazers_count"], "stars")
