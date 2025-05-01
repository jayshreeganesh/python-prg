friends = {"Rachel":"Ross", "Monica":"Chandler","Phoebe":"Joe"}

name = input("Enter a key here : ")
# name = "Monica"
# name = "Janice"


if name in friends.keys():
    print("It is present")