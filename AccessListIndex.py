# Solution 1 - Using Enumerate Method

temp_list = [34,5,61,54,89]

# for index, value in enumerate(temp_list, start=1):
for index, value in enumerate(temp_list):
    print(index, "-", value)

# Solution 2 - Not Using Enumerate Method   
#  
other_list = [34,5,61,54,89]

# print(other_list[3])

for temp_index in range(len(other_list)):
    temp_value = other_list[temp_index]
    print(temp_index, temp_value)
    
