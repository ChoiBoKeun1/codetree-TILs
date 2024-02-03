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

ans = 0
for i in range(1, time_A):
    if pos_A[i] == pos_B[i] and pos_A[i-1] != pos_B[i-1]:
        ans += 1
print(ans)

print(pos_A[:12])
print(pos_B[:12])