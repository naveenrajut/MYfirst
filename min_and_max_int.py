array = [int(x) for x in input().split(" ")]
Min = 0
Max = 0
k = 0
for i in range(5):
    data = 0
    for j in range(5):
        if i != j:
            data = data + array[j]

    if data > Max:
        Max = data
        if k == 0:
            Min = Max
            k += 1
    if data < Min:
        Min = data

print(str(Min)+" "+str(Max))
                
