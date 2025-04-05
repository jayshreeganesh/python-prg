a = 0
b = 1
num = int(input("Enter a number to obtain Fibonacci Sequence : "))

if num == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2,num):
        c = a + b
        a = b
        b = c
        print(c)
