marks = {"John":23,"Lisa":56,"Sid":48}
print(marks)

#Solution 1 - Sort dictionary based on values

sorted_values = sorted(marks.items(), key = lambda x : x[1])
print(sorted_values)

sorted_keys = sorted(marks.items(), key = lambda x : x[0])
print(sorted_keys)

# Solution 2 - Sort only values

sort_dict = sorted(marks.values())
print(sort_dict)