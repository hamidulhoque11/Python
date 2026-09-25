matrix=[
    [10,20,30],
    [3,0,1],
    [10,20,3],
]
print(matrix[0][1])

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()