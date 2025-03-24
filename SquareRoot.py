#Solution-1 (Using Exponentiation)
num = 64
sr = num**(1/2)
print ("The square root of the given number is", sr)

num1 = int(input("Enter a number here : "))
sr1 = num1**(1/2)
print ("The square root of the given number is", sr1)

num2 = int(input("Enter a number here : "))
sr2 = num2**(0.5)
print ("The square root of the given number is", sr2)

#Solution-2 (Using Math Module)
import math
num4 = int(input("Enter a number here : "))
sr4 = math.sqrt(num4)
print("The square root of the given number is ", sr4)