n = int(input())

for i in range(n):
    if i == 0 or i == n-1:
        for _ in range(n):
            print('*',end=" ")
        print()
    
    else:
        print('*',end=' ')
        for _ in range(i-1):
            print('*',end=' ')
        for _ in range(n-i-1):
            print(' ',end=' ')
        print('*',end=' ')
        print()

'''
for i in range(n):
    for j in range(n):
        if i > j or i == 0 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''


'''
i   
0   0 space
1   0 star 3 space
2   1 star 2 space
3   2 star 1 space
4   0 space

'''