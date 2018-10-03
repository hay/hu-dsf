sentence = input("Give me a sentence: ")
senlen = len(sentence)
start = round(senlen * 0.25)
end = round(senlen * 0.75)
newsen = sentence[start:end]
print(newsen)

words = sentence.split(" ")
wordslen = len(words)
start = round(wordslen * 0.25)
end = round(wordslen * 0.75)
newwords = words[start:end]
print(" ".join(newwords))