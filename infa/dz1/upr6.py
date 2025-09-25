lst = input().split()
d = {}
for i in lst:
    d[i] = d.get(i, 0) + 1
for i in lst:
    if d[i] == 1:
        print(i)