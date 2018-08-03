n = int(input())
array = [int(i) for i in input().split(" ")]
Min = abs(array[0] - array[1])
i = j = 0

array = sorted(array)
for i in range(n-1):
    if Min > abs(array[i]-array[i+1]):
        Min = abs(array[i]-array[i+1])

print(Min)
            
