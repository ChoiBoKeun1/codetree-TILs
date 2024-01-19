n = int(input())

num = 9

for i in range(n):
    for j in range(n):
        print(num,end='')
        num -= 1
        if num == 0:
            num = 9
    print()