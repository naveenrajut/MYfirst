if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    runner = -101
    for i in range(len(array)-1):
        if array[i] > array[i+1] and array[i+1] > runner:
            runner = array[i+1]
        elif array[i] < array[i+1] and array[i] > runner:
            runner = array[i]

    print(runner)

