# Solution 1 : using del statement

marks = {"John":89, "Lisa":96, "David":65, "Peter":88}
# marks = {"John":89, "Lisa":96, "David":65, "john":89, "Peter":88}
print(marks)

# del(marks["John"])
# del(marks["john"])
del(marks["Peter"])

print(marks)


# Solution 2 : using pop() function

marks = {"John":89, "Lisa":96, "David":65, "Peter":88}
# marks = {"John":89, "Lisa":96, "David":65, "john":89, "Peter":88}
print(marks)

# marks.pop("john")
# marks.pop("John")
marks.pop("Peter")
print(marks)