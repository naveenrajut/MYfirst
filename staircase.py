num = int(input())
j = num
i = 0
while i <= num and j > 0:
    m = i
    n = j
    while n > 1 :
        print(" ",end = "")
        n -= 1
    while m >= 0:
        print("#",end = "")
        m -= 1
    print("")
    i += 1
    j -= 1
