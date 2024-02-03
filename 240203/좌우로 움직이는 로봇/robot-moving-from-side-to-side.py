MAX_T = 1000000

n,m = map(int,input().split())
pos_A, pos_B = [0] * (MAX_T+1), [0] * (MAX_T+1)

time_A = 1
for _ in range(n):
    t,d = tuple(input().split())
    for _ in range(int(t)):
        pos_A[time_A] = pos_A[time_A - 1] + (1 if d == 'R' else -1)
        time_A += 1

time_B = 1
for _ in range(m):
    t,d = tuple(input().split())
    for _ in range(int(t)):
        pos_B[time_B] = pos_B[time_B - 1] + (1 if d == 'R' else -1)
        time_B += 1


if time_A < time_B:
    for i in range(time_A, time_B):
        pos_A[i] = pos_A[time_A-1]
elif time_A > time_B:
    for i in range(time_B, time_A):
        pos_B[i] = pos_B[time_B-1]

ans = 0
max_time = max(time_A,time_B)
for i in range(1, max_time):
    if pos_A[i] == pos_B[i] and pos_A[i-1] != pos_B[i-1]:
        ans += 1
    
print(ans)