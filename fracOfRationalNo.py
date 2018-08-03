n = int(input())
array = [int(i) for i in input().split(" ")]
pos = neg = zero = 0
length = len(array)
for i in array:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1

print(format(pos/length,'.6f'))
print(format(neg/length,'.6f'))
print(format(zero/length,'.6f'))
