m,n = [int(x) for x in input().split(" ")]
array = [x for x in input().split(" ")]
a = input().split(" ")
a = set(a)
b = input().split(" ")
b = set(b)
result = 0
for i in array:
    if i in a:
        result += 1
    elif i in b:
        result -= 1

print(result)
