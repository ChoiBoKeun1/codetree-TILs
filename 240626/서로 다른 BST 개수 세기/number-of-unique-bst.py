n = int(input())

dp = [0] * (n+1)

dp[0] = 1 # 빈 트리 1개
dp[1] = 1 # 노드 1개인 트리 1개

for nodes in range(2, n +1):
    for root in range(1, nodes +1):
        left = root - 1         # 왼쪽 서브트리 개수
        right = nodes - root    # 오른쪽 서브트리 개수
        dp[nodes] += dp[left] * dp[right]

print(dp[n])