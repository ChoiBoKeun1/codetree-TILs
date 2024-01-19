n = int(input())

num = 0

for i in range(n):
    for _ in range(n):
        if i % 2 == 0:
            num += 1
        else:
            num += 2
        print(num,end=' ')
    print()