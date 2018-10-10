import requests

url = input("Give me an URL:").strip()

req = requests.get(url)

print(f"Data for URL {url}")

if req.status_code != 200:
    print(f"Woops, we got an error: {req.status.code}")
    exit()

for key, val in req.headers.items():
    print(f"{key} : {val}")

print("And here is the text")
print("\n".join(req.text.split("\n")[0:10]))
