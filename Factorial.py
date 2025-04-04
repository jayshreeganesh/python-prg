#Solution 1 - Using for loop

num = int(input("enter a number here : "))

fact = 1

if num < 0 :
    print("Factorial of negative number does not exist")
elif num == 0 :
    print("Factorial of 0 is ", 1)
elif num > 0:
    for i in range (1, num+1):
        fact = fact * i
    print ("The factorial of given number is ",fact)

# Solution 2 - Using RecursionError    

def fact(a):
    if a == 0:
        return 1
    else :
        return ((a) * fact(a-1))
    
num_f = int(input("Enter a number here : "))
fact_num = fact(num_f)
print("Factorial of th given number is ", fact_num)
    