a = input("Enter a number/name here : ")
b = input("Enter a number/name here : ")
c = input("Enter a number/name here : ")

print("The value of a is",a)
print("The value of b is",b)
print("The value of c is",c)

# a,b,c = input("Enter three values here : ").split()
a,b,c = input("Enter three values here : ").split(",")
print("The value of a is",a)
print("The value of b is",b)
print("The value of c is",c)

print("The addition of givent numbers is")
print (int(a) + int(b) + int(c))

a,b,c = [int(x) for x in input("Enter three values").split(",")]
print("The addition of givent numbers is")
# print (int(a) + int(b) + int(c))
print (a + b + c)