n,m = map(int,input().split())

arr = []
arr2 = []

for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)

for _ in range(n):
    row = list(map(int,input().split()))
    arr2.append(row)

answer = [
    [0 for _ in range(m)] for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if arr[i][j] != arr2[i][j]:
            answer[i][j] += 1

for row in answer:
    for n in row:
        print(n, end=' ')
    print()