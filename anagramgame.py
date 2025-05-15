import random

# f = open("word.txt","r")
# a = f.readline()
# words = a.split(",")
# print(words)

words = ["ironman", "thor", "hawkeye", "wanda", "vision"]

word = random.choice(words)

print(word)

jumble = "".join(random.sample(word, len(word)))
print(jumble)

chances = 3

print("~"*30)
print("~~~ Avengers Jumble Bumble ~~~")
print("~"*30)

while chances != 0:
    print("The word is",jumble)

    guess = input("Enter your guessed word : ").lower()
    if guess == word:
        print("correct Guess!!")
        print("You Won!")
        print()
        break
    else:
        chances -= 1
        print("Incorrect Guess!!")
        print("Remaining chances are : ", chances)
        print()
else:
    print("All your chances are exhausted")
    print("You lose")
    print("The correct word is", word)

print("Thank You for playing")