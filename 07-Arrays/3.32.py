matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [3, 8, 3],
    [2, 1, 9]
]
'''print(matrix)

matrix[0],matrix[-1]=matrix[-1],matrix[0]
print(matrix)''' #swaps rows

for row in matrix:
    row[0],row[-1]=row[-1],row[0]
print(matrix)