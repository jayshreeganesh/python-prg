# Solution 1 - Using for loop

A = [[1,2,3],
    [4,5,6]]

T = [[0,0],
     [0,0],
     [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        # print (j)
        T[j][i] = A[i][j]

# print(T)
for r in T:
    print(r)

# Solution 2 - Using List Comprehension
B = [[1,2,3],
     [4,5,6]]

TB = [[B[m][n] for m in range (len(B))] for n in range (len(B[0]))]

# print(TB)

for res in TB:
    print(res)
