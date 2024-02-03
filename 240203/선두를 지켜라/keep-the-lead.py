MAX_T = 1000

n,m = map(int,input().split())
A, B = [0] * (MAX_T+1), [0] * (MAX_T+1)
isFirst = [False,False]

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

answer = 0

i = 1
while A[i] == B[i]:
    i += 1
if A[i] > B[i]:
    isFirst[0] = True
    isFirst[1] = False        
elif A[i] < B[i]:
    isFirst[0] = False
    isFirst[1] = True

for i in range(MAX_T):
    if A[i] != 0 and A[i] == B[i]:
        # A가 B를 추월
        if A[i+1] > B[i+1] and A[i-1] <= B[i-1] and isFirst[1]:
            answer += 1
            isFirst[0] = True
            isFirst[1] = False
        # B가 A를 추월
        elif A[i+1] < B[i+1] and A[i-1] >= B[i-1] and isFirst[0]:
            answer += 1
            isFirst[0] = False
            isFirst[1] = True
print(answer)