# sentence = "Harry Potter and the Goblet of Fire"
# sentence = "Charlie and the Chocolate Factory"

sentence = input("Enter something here : ")

words = sentence.split()

print(words)

for i in range(len(words)):
    words[i] = words[i].lower()

print(words)    

words.sort()
print(words)

for r in words:
    print(r)