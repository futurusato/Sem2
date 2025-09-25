lst = input().split()
d = {}
for i in lst:
    d[i] = d.get(i, 0) + 1
m = d[lst[0]]
k = lst[0]
for i in lst:
    if d[i] > m:
        m = d[i]
        k = i
print(k)