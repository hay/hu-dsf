colors = ["red", "yellow", "blue", "green", "orange"]
emoji = ["🔴", "💛", "🔵", "💚", "🧡"]
sentence = input("Enter a sentence: ")

# Here's a solution where we create a new list, and append the replaced word to it
new_sentence = []
for word in sentence.split(" "):
    if word in colors:
        index = colors.index(word)
        icon = emoji[index]
        print(word + " should be " + icon)
        new_sentence.append(icon)
    else:
        new_sentence.append(word)

new_sentence = " ".join(new_sentence)
print(new_sentence)