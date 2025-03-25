#Solution 1 (Using third variable)

x = 13
y = 12

temp = x
print("The value of temp variable is", temp)

x = y
print("The value of x variable is", x)

y = x
print("The value of y variable is", temp)


#Solution 2 (Without using third variable)
x1 = 12
y1 = 13

x1,y1 = y1,x1

print("The value of x1 variable is ", x1)
print("The value of y1 variable is ", y1)

#Solution 3 (Without using third variable)
a = 12
b = 13

a = a + b
print("The value of a variable is ", a)
b = a - b
print("The value of b variable is ", b)
a = a - b
print("The value of a variable is ", a)

print("The value of a variable is ", a)
print("The value of b variable is ", b)