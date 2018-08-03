n,m = input().split()
n = int(n)
m = int(m)
d = {}
array = []

for i in range(1,n+1):
    d[i] = 0

for i in range(m):
    array.append([int(x) for x in input().split(" ")])

for i in range(m):
    for j in range(array[i][0],array[i][1]+1):
        d[j] = d[j]+array[i][2]

Max = 0

for i in range(1,n+1):
    if d[i] > Max:
        Max = d[i]

print(Max)
        

