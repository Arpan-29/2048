n = int(input())
arr = [int(x) for x in input().split()]
k = int(input())

for i in range(n + 1 - k) :
    for j in range(i, i + k) :
        if arr[j] < 0 :
            print(arr[j], end = ' ')
            break
    else :
        print(0, end = ' ')
        