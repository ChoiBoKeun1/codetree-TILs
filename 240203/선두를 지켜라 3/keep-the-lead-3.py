n,m = map(int,input().split())
pos_A, pos_B = [0] * 1001, [0] * 1001

time_a = 1
for _ in range(n):
    v,t = map(int,input().split())
    for i in range(t):
        pos_A[time_a] = pos_A[time_a - 1] + v
    time_a += 1

time_b = 1
for _ in range(m):
    v,t = map(int,input().split())
    for i in range(t):
        pos_B[time_b] = pos_B[time_b - 1] + v
    time_b += 1

honor = [0] * 1001

# honor list의 idx 시간에 누가 명예의 전당에 있는지 기록한다.
# honor[1] : A, [2] : B, [3]: A,B 둘다.
for i in range(time_a + 1):
    if pos_A[i] > pos_B[i]:
        honor[i] = 1
    elif pos_A[i] < pos_B[i]:
        honor[i] = 2
    else:
        honor[i] = 3

answer = 1
for i in range(1,time_a):
    if honor[i] != honor[i+1]:
        answer += 1

print(answer)