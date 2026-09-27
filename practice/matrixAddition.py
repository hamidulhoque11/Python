A=[
    [1 , 2 , 3],
    [1 , 2 , 3],
]
B=[
    [1 , 2 , 3],
    [1 , 2 , 3],
]
print("A=")
for x in A:
    print (x)
print("B=")
for x in B:
    print (x)

result=[
    [A[i][j]+ B[i][j] for j in range(3)]
    for i in range(2)
]
print("A+B=")
for x in result:
    print(x)