def NNS(n):
    if n<= 1:
        return n
    else :
        return n + NNS(n-1)
    
# print(NNS(10))  
  
num = int(input("Enter a number :"))

if num < 0:
    print("Please enter positive number")
else:
    print("The Sum of Natural Number upto given range is", NNS(num))
