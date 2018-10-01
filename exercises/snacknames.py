names = ["Tinus", "Barrie", "Hans"]
snacks = []

for name in names:
    length = len(name)
    print(name + ", that's a name of " + str(length) + " chars")
    snack = input("Enter favourite snack ")
    snacks.append(snack)

# This is a solution where we manually keep track of the index
print("Solution using manually tracked index")
index = 0
for name in names:
    snack = snacks[index]
    print(name + "'s favourite snack is: " + snack)
    index += 1

# This is another solution where we use the enumerate function to get the index
print("Soltion using enumerate")
for index, name in enumerate(names):
    snack = snacks[index]
    print(name + "'s favourite snack is: " + snack)

# And here is a solution where we use the index() method of the names list
print("Solution using the index() method")
for name in names:
    index = names.index(name)
    snack = snacks[index]
    print(name + "'s favourite snack is: " + snack)