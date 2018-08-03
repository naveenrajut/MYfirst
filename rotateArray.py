n,d = input().split(" ")
array = [int(i) for i in input().split(" ")]
length = len(array)
start = length%int(d)
result = []
if start == 0 and type(length//int(d)) != int:
    for i in array[length-start:]:
        result.append(i)
    for i in array[:length-start]:
        result.append(i)
else:
    for i in array[int(d):]:
        result.append(i)
    for i in array[:int(d)+1]:
        result.append(i)
print(result)
