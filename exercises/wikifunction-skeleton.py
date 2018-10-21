import requests

title = "Japanese cuisine"
url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
req = requests.get(url)

if req.status_code != 200:
    print(f"We got an error: {req.status_code}")
    exit()

data = req.json()
print(data["extract"])
print(data["description"])