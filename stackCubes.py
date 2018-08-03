t = int(input())
for i in range(t):
    n = int(input())
    array = [int(x) for x in input().split(" ")]
    start = 0
    end = len(array)-1
    if array[start] >= array[end]:
        previous = array[start]
        start += 1
    else:
        previous = array[end]
        end -= 1
    while True:
        if start =< end:
            if array[start] == array[end] and previous >= array[start]:
                previous = array[start]
                start += 1

            elif array[start] > array[end] and previous >= array[start]:
                previous = array[start]
                start += 1

            elif array[start] < array[end] and previous >= array[end]:
                previous = array[end]
                end -= 1

            else:
                print("No")
                break

        else:
            print("Yes")
            break
