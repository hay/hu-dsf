from bs4 import BeautifulSoup

with open("restaurant.html") as f:
    page = BeautifulSoup(f, "lxml")

title = page.select("title")
items = page.select("ul > li")
order = page.select(".order")

print("Title: " + title[0].get_text())

for item in items:
    print(item.get_text())

print("Order url: " + order[0]["href"])