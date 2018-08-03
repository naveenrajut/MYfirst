N = int(input())
array = [int(i) for i in input().split(" ")]
array = sorted(array,reverse=True)
Min = 0

for i in range(N):
    Min = Min + ((2**i)*array[i])
    

print(Min)
