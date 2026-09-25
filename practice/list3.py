n=input()
my_list=list(map(int,n.split()))
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print("reverse:",my_list)
for x in my_list:
    print(x,end=" ")