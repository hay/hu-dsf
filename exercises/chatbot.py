import requests

def welcome():
    print("Hello!")

while True:
    q = input("Me: ").lower().strip()

    if "hi" in q:
        welcome()
    else:
        print("I don't know what you are saying")
