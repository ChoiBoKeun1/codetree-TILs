n,m,p = map(int,input().split())
arr = [0] + [
    tuple(map(str,input().split()))
    for _ in range(m)
]

people = [False] * n

for i in range(1,m+1):
    if i >= p:
        c,u = arr[i]
        people[ord(c)-65] = True

for i in range(n):
    if not people[i]:
        print(chr(i+65),end=' ')