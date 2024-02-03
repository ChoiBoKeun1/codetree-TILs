MAX_T = 1000000

n,m = map(int,input().split())
A, B = [0] * (MAX_T+1), [0] * (MAX_T+1)

time_a = 1
for _ in range(n):
    v,t = map(int,input().split())
    for _ in range(t):
        A[time_a] = A[time_a - 1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v,t = map(int, input().split())
    for _ in range(t):
        B[time_b] = B[time_b - 1] + v
        time_b += 1

leader, answer = 0, 0
for i in range(1, time_a):
    if A[i] > B[i]:
        if leader == 2:
            answer += 1
        leader = 1
    elif A[i] < B[i]:
        if leader == 1:
            answer += 1
        leader = 2

print(answer)