import requests
import json

title = input("Enter an article: ").strip().replace(" ", "_")
languages = {
    "en" : "English",
    "es" : "Espanol",
    "nl" : "Nederlands"
}

for lang, langname in languages.items():
    print(f"Looking up in {langname}")
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{title}"

    req = requests.get(url)

    if req.status_code != 200:
        print(f"We got an error: {req.status_code}")
        print("")
    else:
        data = json.loads(req.text)
        description = data["description"]
        extract = data["extract"]
        print(f"{title}: {description}")
        print(extract)
        print("")