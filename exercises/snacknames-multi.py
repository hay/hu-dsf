friends = [
    ["Barrie"],
    ["Tinus"],
    ["Hans"]
]

for friend in friends:
    name = friend[0]
    length = len(name)
    print(name + " is a name of " + str(length) + " characters")
    snack = input("What does " + name + " like? ")
    friend.append(snack)
    
for friend in friends:
    print(friend[0] + " likes " + friend[1])