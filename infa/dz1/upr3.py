a = input()
n = int(len(a))
f = 0
c = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
for i in range (0, len(a)):
    if a[i]!=a[len(a)-i-1]:
        f=1
if f==1:
    for i in range(0, len(a)):
        if (a[i]=='E' and a[len(a) - i - 1]=='3') or (a[i]=='J' and a[len(a) - i - 1]=='L') or (a[i]=='5' and a[len(a) - i - 1]=='2') or (a[i]=='2' and a[len(a) - i - 1]=='5'):
            f = 2
if f==1:
    print (a, "is not a palindrome")
elif f==2:
    print (a, "is a mirrored string")
if f==0:
    for i in range(0, len(a)):
        if a[i] not in c:
            f=3
if f==3:
    print(a, "is a regular palindrome")
if f==0:
    print(a, "is a mirrored palindrome")
