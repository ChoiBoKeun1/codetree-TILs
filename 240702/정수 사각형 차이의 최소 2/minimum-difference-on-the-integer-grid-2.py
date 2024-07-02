N = int(input())
max_number = 100
gMap = [[float('inf')] * N for _ in range(N)]
for j in range(N):
    letter = list(map(int, input().split()))
    for i in range(N):
        gMap[j][i] = letter[i]
# 지나가는데 최댓값이 가장 작아야 하고, 
# 지나가는데 최솟값이 가장 커야 한다.

# 1번 조건은, 위 왼쪽 살폈을 때 가장 작은거 고르는데, 내가 그것보다 크면 어쩔 수 없이 내가 max값이 됨
# 2번 조건은, 위 왼쪽 살폈을 때 가장 큰거 고르는데, 내가 그것보다 작으면 어쩔 수 없이 내가 min 값이 됨
# --> 이런방식으로 하면 1번조건과 2번조건 만족하는 루트가 다르다. 그래서 이러면 안되고, 최솟값을 정해서, 
# 그 최솟값 이하의 숫자로는 지나가지 않도록 하는 방향으로 코딩하자. 
# 즉, lower bound를 설정하고, 1번조건만 사용해서 코딩하자. 

def MaxUpdate(y, x, Dp): 
    left = Dp[y][x-1] if 0 <= x-1 else float('inf')
    up = Dp[y-1][x] if 0 <= y-1 else float('inf')

    # 1번 조건은, 위 왼쪽 살폈을 때 가장 작은거 고르는데, 내가 그것보다 크면 어쩔 수 없이 내가 max값이 됨
    Dp[y][x] = max(min(left,up), gMap[y][x]) # 이거 시작점이면 inf 나와버림. 그래서 시작점은 제외해야함. 
    
ans = float('inf')

for lower_bound in range(1, max_number + 1):
    Dp = [[0] * N for _ in range(N)]
    
    for j in range(N):
         for i in range(N):
            if gMap[j][i] < lower_bound:
                Dp[j][i] = float('inf') # 못가는 길은 inf로 만들어라. 
                
    Dp[0][0] = gMap[0][0]
                
    for j in range(N):
        for i in range(N):
            if (j == 0 and i == 0) or Dp[j][i] == float('inf'): # 첫번째 그냥 지나가
                continue
            MaxUpdate(j, i, Dp)

    upper_bound = Dp[N-1][N-1]

    real_lower_bound = float('inf') # 진짜 lower bound는 Dp가 Upperbound보다 작거나 같으면서 gMap이 가장 작은 친구임. 이러면 시작점도 포함됨. 
    for j in range(N):
        for i in range(N):
            if Dp[j][i] <= upper_bound:
                real_lower_bound = min(gMap[j][i], real_lower_bound)

    if upper_bound == float('inf'): # 결국 갈 수 있는 길이 없다.
        continue

    ans = min(ans, upper_bound - real_lower_bound)
print(ans)