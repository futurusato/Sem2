from collections import Counter
lst = input().split()
res = [item for item, count in Counter(lst).items() if count == 1]
print(res)