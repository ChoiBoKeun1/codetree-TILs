n,m = map(int,input().split())
A = [0]
B = [0]

for _ in range(n):
    cmd, t = map(str,input().split())
    t = int(t)
    if cmd == 'R':
        for _ in range(t):
            A.append(A[len(A)-1]+1)
    else:
        for _ in range(t):
            A.append(A[len(A)-1]-1)

for _ in range(m):
    cmd, t = map(str,input().split())
    t = int(t)
    if cmd == 'R':
        for _ in range(t):
            B.append(B[len(B)-1]+1)
    else:
        for _ in range(t):
            B.append(B[len(B)-1]-1)


for i in range(1,len(A)):
    if A[i] == B[i]:
        print(i)
        break