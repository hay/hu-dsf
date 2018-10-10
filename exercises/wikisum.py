import requests
import json

title = input("Enter an article: ").strip().replace(" ", "_")
url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

req = requests.get(url)

if req.status_code != 200:
    print(f"We got an error: {req.status_code}")
    exit()

data = json.loads(req.text)
display_title = data["titles"]["display"]
description = data["description"]
extract = data["extract"]
print(f"{display_title}: {description}")
print("-" * 80)
print(extract)