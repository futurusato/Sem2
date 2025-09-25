with open("input.txt", "r") as f:
    l = f.read()
s = 0
for i in range(1, len(l)):
    if l[i] in '.?!' and l[i-1] not in '.?!':
        s=s+1
print(s)



