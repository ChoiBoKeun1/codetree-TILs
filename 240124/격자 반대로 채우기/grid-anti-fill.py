n = int(input())

num = 1

arr = [
    [0 for _ in range(n)] for _ in range(n)
]

if n % 2 == 0:
    for j in range(n-1,-1,-1):
        if j % 2 != 0:
            for i in range(n-1,-1,-1):
                arr[i][j] = num
                num += 1
        else:
            for i in range(n):
                arr[i][j] = num
                num += 1
else:  
    for j in range(n-1,-1,-1):
        if j % 2 == 0:
            for i in range(n-1,-1,-1):
                arr[i][j] = num
                num += 1
        else:
            for i in range(n):
                arr[i][j] = num
                num += 1




for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()