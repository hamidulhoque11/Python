A=[
    [1,2,3],
    [1,2,3],
    [1,2,3],
]
B=[
    [4,5,6],
    [7,8,9],
    [10,11,12],
]
print("A=")
for x in A:
    print(x)
print()
print("B=")
for x in B:
    print(x)
print("A+B=")
result=[]
for row in range(3):
    matrix_row=[]
    for col in range(3):
        matrix_row.append(A[row][col]+B[row][col])
    result.append(matrix_row)
print("A+B=")
for x in result:
    print(x)
