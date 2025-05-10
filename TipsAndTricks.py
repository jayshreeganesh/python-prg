# Multiple checks in if statement

marks = 80

if marks == 90 or marks == 80 or marks == 95:
    print("Good Job!")

if 80 in [90, 80, 95]:
    print("Good Job!")

# Shorthand if-else statement

marks = 80

if marks > 90:
    print("Excellent Work")
else:
    print("Good job!")

print("Excellent Work") if marks > 90 else print("Good Job!")

# List Comprehension

l = [50, 30, 20, 60, 20, 40]

a = []
for i in l:
    a.append(i*2)
print("Using for loop",a)

x = [i*2 for i in l]
print("Using LC", x)

# Using Enumerate function

l = [10, 40, 20, 30, 40]

index = 0
for i in l:
    print(index, i)
    index += 1

for i in enumerate(l):
    print(i)
    

# Using _ as seperator

# num1 = 9000000
# num2 = 10000

num1 = 90_00_000
num2 = 10_000

sum_of_two = (num1+num2)
print (sum_of_two)
print(f'{sum_of_two:,}')


# Lambda function

def square(x):
    return x*x

print(square(4))

a = lambda b: b**2
print(a(4))


# Using Zip functions

print('Joe has scored 90 marks in math')
print("Chandler has scored 60 marks in art")
print("Ross has scored 50 marks in biology")
print("Phoebe has scored 95 marks in psychology")

print()

names = ["Joe", "chandler", "Ross", "Phoebe"]
marks = [90, 60, 50, 95]
subjects = ["math", "art", "biology", "psychology"]

for name, mark, subject in zip(names, marks, subjects):
    print(name, "has scored", mark, "marks in", subject)

# Protect passwords in terminal

username = input("Enter Username : ")    
password = input("Enter Password : ")
print("Login Successful")

from getpass import getpass

username = input("enter Username : ")
password = getpass("enter Password : ")
print(password)


# Using sets to sort the unique values

l = [10, 30, 20, 40, 30, 40, 60, 40, 50, 30, 20]

print(l)

my_set = set(l)
print(my_set)
print(list(my_set))



# Format string with f string

name = "Ayushi"

print("my name is", name)
print(f'my name is {name}')

num1 = 16
num2 = 34

print ("The addition of", num1, "and", num2, "is", num1+num2)
print (f'The addition of {num1} and {num2} is {num1+num2}')


# Using sorted to sort te complex iterables

l = [67, 30, 56, 28, 96, 12]

sorted_list = sorted(l)
print(sorted_list)

reverse_sorted_list = sorted(l, reverse=True)
print(reverse_sorted_list)

dl = [{"name":"Ross", "marks":87},
      {"name":"Joe", "marks":78},
      {"name":"chandler", "marks":67},
      {"name":"Gunther", "marks":96}]

sorted_data = (sorted(dl, key=lambda x:x["marks"]))
print(sorted_data)

for i in sorted_data:
    print(i)


# Merge Dictionaries using **

dict1 = {"name":"Ross", "marks":89}    
dict2 = {"name":"Ross", "Hobbies":"Singing"}

md = {**dict1, **dict2}
print(md)

# Unpacking using _ and * variable

# a, b, c = (10, 20)
# a, b, c = (10, 20, 30, 40, 50)
# print(a)

a, b, *c = (10, 20, 30, 40, 50)
print(a)
print(b)
print(c)

a, b, *_ = (10, 20, 30, 40, 50)
print(a)
print(b)
# print(c)

a, b, *c, d = (10, 20, 30, 40, 50)
print(a)
print(b)
print(c)
print(d)

# Generators to save memory

import sys

l = [i for i in range(90000)]
print (sum(l))
print(sys.getsizeof(l),"bytes")

g = (j for j in range(90000))
print (sum(g))
print(sys.getsizeof(g),"bytes")


# Using .join to concatenate strings

l = ["Welcome", "to", "WsCube", "Tech"]

a = "" 
for i in l:
    a+=i + " "
print(a)

a = " ".join(l)
print(a)
