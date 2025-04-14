def fibo (n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
# print(fibo(5))

num = int(input("Enter a number of terms here : "))
if num < 0:
    print("Please enter positive number : ")
else:
    print("Fibonacci Sequence")
    for i in range(num):
        print(fibo(i))
