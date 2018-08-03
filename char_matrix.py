t = int(input())

def check():
    n = int(input())
    previous = 0
    statement = True
    for j in range(n):
        current = 0
        array = list(input())
        for k in array:
            current = current + ord(k)
        print(current,"current")
        print(previous,"previous")
        if current > previous:
            previous = current
        else:
            statement = False
    if statement:
        return True
    else:
        return False
            
for i in range(t):
    condition = check()
    
    if condition:
        print("YES")
    else:
        print("NO")



