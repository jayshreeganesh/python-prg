# Solution 1 - Using Dictionary

# sentence = "Harry potter and Goblet of Fire"
# sentence = "Harry potter and Prisoner of Azkaban"
sentence = input("Enter sentence here : ")

print(sentence)

sentence = sentence.casefold()
vowels = "aeiou"
print(sentence)

count = {}.fromkeys(vowels,0)
print(count)

for char in sentence:
    if char in count:
        count[char] +=1

print(count)

# Solution 2 - Using  List and Dictionay comprehension

other_sentence = input("Enter other sentence here : ")
other_sentence = other_sentence.casefold()
print(other_sentence)
other_vowels = "aeiou"
other_count = {o_key:sum([1 for o_char in other_sentence if o_char == o_key])for o_key in other_vowels}
print(other_count)