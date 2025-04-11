def findHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range (1, smaller+1):
        if(x%i==0) and (y%i==0):
            hcf = i
    return hcf
    
x = int(input("Enter 1st number here : "))    
y = int(input("Enter 2nd number here : "))
print("The HCF or GCD of given two number x =", x, "and y =", y, "is : ", findHCF(x,y))    