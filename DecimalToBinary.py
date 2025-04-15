def ConvertToBinary (n):
    if n > 1:
        ConvertToBinary(n//2)
    print(n%2, end = "")

num = int(input("Enter a number here : "))
print("The binary of the given number is : ")
ConvertToBinary(num)    