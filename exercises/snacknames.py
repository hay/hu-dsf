names = ["Tinus", "Barrie", "Hans"]
snacks = []

index = 0
for name in names:
    length = len(name)
    print(name + ", that's a name of " + str(length) + " chars")
    snack = input("Enter favourite snack ")
    snacks.append(snack)
    index += 1

index = 0
for name in names:
    snack = snacks[index]
    print(name + "'s favourite snack is: " + snack)
    index += 1