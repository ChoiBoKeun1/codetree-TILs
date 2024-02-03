MAX_T = 1000000
n,m = map(int,input().split())
pos_A, pos_B = [0] * (MAX_T+1), [0] * (MAX_T+1)

time_a = 1
for _ in range(n):
    v,t = map(int,input().split())
    for _ in range(t):
        pos_A[time_a] = pos_A[time_a - 1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v,t = map(int,input().split())
    for _ in range(t):
        pos_B[time_b] = pos_B[time_b - 1] + v
        time_b += 1


# leader == 1 : A, 2 : B, 3: A/B 둘다.
leader,answer = 0,0
for i in range(1,time_a):
    if pos_A[i] > pos_B[i]:
        if leader != 1:
            answer += 1
        leader = 1
    elif pos_A[i] < pos_B[i]:
        if leader != 2:
            answer += 1
        leader = 2
    else:
        if leader != 3:
            answer += 1
        leader = 3


print(answer)