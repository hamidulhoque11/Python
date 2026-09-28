A=[
    [10,5,0],
    [20,4,30],
    [10,2,2],
]
B=[
    [11,1,11],
    [5,4,7],
    [10,1,2],
]
print("A=")
for x in A:
    print(x)
print()
print("B")
for x in B:
    print(x)
print()
resutlt=[
    [A[row][col]-B[row][col] for col in range(3) ]
    for row in range(3)
]

print("A-B=")
for x in resutlt:
    print(x)