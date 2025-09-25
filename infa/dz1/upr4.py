lst = input().split()
for i in range(0, len(lst)-1, 2):
    n = lst[i+1]
    lst[i+1]=lst[i]
    lst[i]=n
print(lst)