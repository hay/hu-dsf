import requests

def api_call(title):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    req = requests.get(url)

    if req.status_code != 200:
        print(f"We got an error: {req.status_code}")
        exit()

    return req.json()

def lookup(title, value):
    data = api_call(title)

    if value == "description":
        return data["description"]
    elif value == "extract":
        return data["extract"]
    elif value == "url":
        return data["content_urls"]["desktop"]["page"]
    else:
        return "Invalid value!"

title = input("Give an article you want to lookup: ").strip()
value = input("Do you want the description, extract or url? ").strip().lower()
data = lookup(title, value)
print(f"Here is the {value} for {title}:")
print(data)