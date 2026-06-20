import requests
params = {
    "shouji": "18817391969",
    "appkey": "0c818521d38759e1"
}

r = requests.get(url="https://api.binstd.com/shouji/query", params=params)
print(r.status_code)
print(r.json())