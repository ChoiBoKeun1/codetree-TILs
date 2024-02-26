import sys

INT_MAX = sys.maxsize

n = int(input())
seats = list(input())

# 1단계. 인접한 쌍들 중 가장 먼 1 간의 쌍 찾기.
max_dist = 0
max_i, max_j = 0,0
for i in range(n):
        for j in range(i+1,n):
            if seats[i] == '1' and seats[j] == '1':
                if max_dist < j-i:
                    max_dist = j-i
                    max_i, max_j = i,j
                break

# 1-2 단계. 맨 앞이랑 맨 뒤가 비어있을때, 여기에 사람을 배정하면 최적의 위치일까?
# 맨앞/맨뒤 에 사람을 배정했을때, 걔랑 가장 먼 '1' 이랑의 거리를 측정
max_dist2 = -1
max_idx = -1
if seats[0] == '0':
    dist = 0
    for i in range(n):
        if seats[i] == '1':
            break
        dist += 1
    
    if max_dist2 < dist:
        max_dist2 = dist
        max_idx = 0

if seats[n-1] == '0':
    dist = 0
    for i in range(n-1,-1,-1):
        if seats[i] == '1':
            break
        dist += 1
    
    if max_dist2 < dist:
        max_dist2 = dist
        max_idx = n-1

# 2단계. 사람을 배정한다.
# 최적의 위치는 가장 먼 1 사이 중 가운데에 있는 0 위치 or 맨앞 or 맨뒤 셋중 하나다.
# 최적의 위치가 맨앞 or 맨뒤인 경우
if max_dist2 >= max_dist // 2:
    seats[max_idx] = '1'
# 최적의 위치가 '가장 먼 1 사이 중 가운데에 있는 0 위치' 인 경우.
else:
    seats[(max_i+max_j) // 2] = '1'

ans = INT_MAX
for i in range(n):
    for j in range(i+1, n):
        if seats[i] == '1' and seats[j] == '1':
            ans = min(ans, j-i)
            break

print(ans)