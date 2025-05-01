# Solution 1 - Using + operator

l1 = [3, 6, 8, 2, "a", "j"]
l2 = [3, 6, "k", "f", "j"]

l12 = l1 + l2

print(l12)

# Solution 2 - Using Unique Values

l_1 = [3, 6, 8, 2, "a", "j"]
l_2 = [3, 6, "k", "f", "j"]

# l_3 = {2, 5, 6, 1, 2, 5, 6}
# print(l_3)

l_4 = list(set(l_1 + l_2))
print(l_4)

# Solution 3 - Using extend() function

l_5 = [3, 6, 8, 2, "a", "j"]
l_6 = [3, 6, "k", "f", "j"]

l_5.extend(l_6)
print(l_5)
