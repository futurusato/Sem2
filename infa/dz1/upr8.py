lst = input().split()
for item in lst:
    n = 0
    for i in range (0, len(lst)):
        if (lst[i]<item):
            n=n+1
    if n == (len(lst)-1)//2:
        print(item)