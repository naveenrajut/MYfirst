string = input()
array = [0]*26
for i in string:
    array[ord(i)-97] += 1

max1 = max2 = max3 = 0
index1 = index2 = index3 = index = 0
print(array)
for i in array:
    if i > max1:
        max1 = i
        index1 = index

    index += 1
array[index1] = index = 0
print(array)
for i in array:
    if i > max2:
        max2 = i
        index2 = index
    index += 1
array[index2] = index = 0
print(array)
for i in array:
    if i > max3:
        max3 = i
        index3 = index
    index += 1

print(chr(97+index1)+" "+str(max1))
print(chr(97+index2)+" "+str(max2))
print(chr(97+index3)+" "+str(max3))
