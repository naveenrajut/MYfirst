n = int(input())
array = [int(i) for i in input().split(" ")]
Max = 0
for i in array:
    if i > Max:
        Max = i
        count = 0
        count += 1
    elif i == Max:
        count += 1

print(count)
