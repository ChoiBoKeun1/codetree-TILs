n = int(input())

for i in range(n):
    if i % 2 == 0:
        for _ in range(n- int(i/2)):
            print('*',end=' ')
    else:
        for _ in range(int((i+1)/2)):
            print('*',end=' ')
    print()

for i in range(n,0,-1):
    if i % 2 != 0:
        for _ in range(n- int(i/2)):
            print('*',end=' ')
    else:
        for _ in range(int((i+1)/2)):
            print('*',end=' ')
    print()