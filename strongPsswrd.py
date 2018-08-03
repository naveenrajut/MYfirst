def isStrong(N,string):
    lowerCase = set(map(chr,range(97,123)))
    upperCase = set(map(chr,range(65,91)))
    numbers = set(map(chr,range(48,58)))
    special = set(map(chr,range(33,48)))
    special.add(64)
    l=u=n=s=count = 0
    for i in string:
        if i in lowerCase:
            l += 1
        elif i in upperCase:
            u += 1
        elif i in numbers:
            n += 1
        elif i in special:
            s += 1
    if s == 0:
        count += 1
    if u == 0:
        count += 1
    if l == 0:
        count += 1
    if n == 0:
        count += 1
    if N < 6:
        N += count
        while True:
            if N < 6:
                N += 1
                count += 1
            else:
                break
        print(count)
    else:
        print(count)
    


if __name__ == "__main__":
    n = int(input())
    string = input()
    isStrong(n,string)
