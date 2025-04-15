def fact (n):
    if n == 1:
        return n
    else:
        return n * fact (n-1)
    
# print(fact(5))

num = int(input("Enter a number here : "))

if num <= 0:
    #print("Please enter positive number")
    print("Factorial of number less than 1 does not exist")
else:
    print("Factorial of given number is : ", fact(num))
