import requests

url = "https://api.github.com/repos/psf/requests/pulls"
resp = requests.get(url, params={"state": "open", "per_page": 10}, timeout=10)
resp.raise_for_status()

for pr in resp.json():
    print(pr["title"], "|", pr["user"]["login"], "|", pr["created_at"])
    