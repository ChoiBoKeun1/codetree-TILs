n = int(input())

A = 65

for i in range(n):
    for _ in range(i):
        print(' ',end=' ')
    for _ in range(n,i,-1):
        print(chr(A),end=' ')
        A += 1
        if A == 91:
            A = 65
    print()