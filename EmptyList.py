# Solution 1 - Using boolean operation

my_list = []
# my_list = [12]
# my_list = [12, 4, 5]

# print(bool(my_list))

if not my_list:
    print("The list is empty")

# Solution 2 - Using len function

temp_list = []
# temp_list = [1, 2, 3, 4, 5]
print(len(temp_list))
if len(temp_list) == 0:
    print("The list is empty")

# Solution 3 - Using [] brackets

other_list = []
# other_list = [12, 4, 56, 7]

if other_list == []:
    print("The list is empty")