string = input()
array = list()
for i in string:
    array.append(ord(i))

array = sorted(array)
previous = 0
current = 1
lowerCase = set(range(97,123))
upperCase = set(range(65,91))
numbers = set(range(48,58))
result = []
for i in array:
    if i in lowerCase:
        result.append(chr(i))

for i in array:
    if i in upperCase:
        result.append(chr(i))

for i in array:
    if i in numbers and i & 1:
        result.append(chr(i))

for i in array:
    if i in numbers and i%2 == 0:
        result.append(chr(i))

print("".join(str(x) for x in result))
