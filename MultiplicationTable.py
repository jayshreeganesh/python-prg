# Solution 1 - with for loop

n = int(input("Enter a number here : "))

for i in range(1,13):
    print(n,"x",i,"=",n*i)

# Solution 2 with while loop

m = int(input("Enter a number here : "))
j = 0
while j<=12:
    print(m,"x",j,"=",m*j)
    j = j + 1 