# Solutin 1 - using for loop

num = int(input("Enter a number here : "))

print("The numbers divisible by ", num, " are : ")
for i in range(1,100):
    if i % num == 0:
        print(i)

# Solution 2 - using list, lambda function and filter

# l = [13,45,23,26,56,34]
l = [39,48,26,98,33,67,87]
print(l)
result = list(filter(lambda x : x % num == 0, l))
print("The numbers divisible by ", num, "are ", result)