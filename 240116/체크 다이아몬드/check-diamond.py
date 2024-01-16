n = int(input())

# 가로세로 2n-1 크기

for i in range(1, n+1):
    for _ in range(n-i):
        print(' ',end='')    
    for _ in range(i):
        print('*',end=' ')
    print()

for i in range(n-1, 0, -1):
    for _ in range(n-i):
        print(' ',end='')    
    for _ in range(i):
        print('*',end=' ')
    print()