normal_time = [12,60,60]
military_time = [24,60,60]
string_time = input()
if "PM" in string_time:
    string_time = string_time[:8]
    array =[int(i) for i in string_time.split(":")]
    if array[0] == 12:
        print(":".join(str(i).zfill(2) for i in array))
        
    else:
        for i in range(3):
            array[i] = abs(array[i] - normal_time[i])

        for i in range(3):
            array[i] = abs(array[i] - military_time[i])

        print(":".join(str(i).zfill(2) for i in array))

else:
    string_time = string_time[:8]
    array =[int(i) for i in string_time.split(":")]
    if array[0] == 12:
        array[0] = 00
    print(":".join(str(i).zfill(2) for i in array))
