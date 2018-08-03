import random
a,b,c = input().split(" ")
q = int(input())
N = int(input())
array = []
count = 0

def miller_rabin(number,k):
    multiplier = number-1
    power = 0
    if number == 2:
        return True
    if not number & 1 or number < 3:
        return False
    while multiplier%2 == 0:
        power += 1
        multiplier //= 2
    for i in range(k):
        a = random.randrange(2,number)
        t = pow(a,multiplier,number)
        if t == 1 or t == number-1:
            result = True
        for j in range(power):
            t = pow(t,2,number)
            if t == 1:
                return False
            if t == number-1:
                return True
    return False

for k in range(N):
    polynomial = (int(a)*(k**1))+(int(b)*(k**1))+int(c)
    print(polynomial)
    condition = miller_rabin(polynomial,5)
    if condition:
        array.append(polynomial)
        count += 1
print(array,count)
