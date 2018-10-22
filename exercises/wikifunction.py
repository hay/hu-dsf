import requests

def lookup(title, value):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    req = requests.get(url)

    if req.status_code != 200:
        print(f"We got an error: {req.status_code}")
        exit()

    data = req.json()

    if value == "description":
        return data["description"]
    elif value == "extract":
        return data["extract"]
    else:
        return "Invalid value!"

title = input("Give an article you want to lookup: ").strip()
value = input("Do you want the description or extract? ").strip().lower()
data = lookup(title, value)
print(f"Here is the {value} for {title}:")
print(data)