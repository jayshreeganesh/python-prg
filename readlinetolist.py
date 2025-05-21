# Solution 1 : Using readLines()

f = open("file.txt", "r")
lines = f.readlines()

print(lines)

new_lines = [x.strip() for x in lines]
print(new_lines)

# Solution 2 : Using For Loop and List Comprehension

f = open("file.txt","r")

line = [line for line in f]
print(line)

new_lines = [x.strip() for x in line]
print(new_lines)