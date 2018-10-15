# This is the 'refactor' version of snacknames, refactored!
friends = [
    {
        "name" : "Tinus",
    },
    {
        "name" : "Barrie"
    },
    {
        "name" : "Hans"
    }
]

for item in friends:
    name = item["name"]
    name_len = len(name)
    print(f"'{name}' has {name_len} characters")
    snack = input(f"{name}, what is your favourite snack? ")
    item["snack"] = snack

for item in friends:
    name = item["name"]
    snack = item["snack"]
    print(f"{name} likes {snack}")