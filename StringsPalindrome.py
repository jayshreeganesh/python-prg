a = input("enter a word here : ")

rev = a[::-1]

if a == rev:
    print("It is palindrome")
else:
    print("It is not palindrome")