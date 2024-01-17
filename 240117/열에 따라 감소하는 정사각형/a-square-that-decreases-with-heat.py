n = int(input())

input_n = n

for i in range(input_n):
    for j in range(input_n):
        print(n, end=' ')
        n -= 1
    print()
    n = input_n