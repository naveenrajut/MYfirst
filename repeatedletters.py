from collections import OrderedDict
d = OrderedDict()
n = int(input())
for i in range(n):
    key = input()
    if key not in d.keys():
        d[key] = 1
    else:
        d[key] += 1
print(len(d))
for i in d.values():
    print(i,end = " ")
