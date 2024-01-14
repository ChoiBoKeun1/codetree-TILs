n = int(input())

for i in range(n,0,-1):
    # 좌측 삼각형
    for _ in range(i):
        print('*',end='')
    # 중간에 공백
    for _ in range(2*(n-i)):
        print(' ',end='')
    # 우측 삼각형
    for _ in range(i):
        print('*',end='')
    print()