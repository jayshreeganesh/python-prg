""" A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[9,8,7],
     [6,5,4],
     [3,2,1]] """

A = [[1,5,8],
     [4,6,7],
     [7,2,3]]

B = [[4,5,6],
     [9,8,1],
     [3,5,6]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

# print(result)
for r in result:
    print(r)
                   