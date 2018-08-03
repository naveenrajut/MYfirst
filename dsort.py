m,n = input().split(" ")
m = int(m)
n = int(n)
array = []
for i in range(m):
    a = [int(x) for x in input().split(" ")]
    array.append(a)
k = int(input())
for i in range(m-1):
    for j in range(i+1,m):
        if array[i][k] > array[j][k]:
            (array[i],array[j]) = (array[j],array[i])

for i in array:
    print("")
    for j in i:
        print(j,end=" ")


