n = int(input())
arr = list(map(int,input().split()))

# inc_dp[i] : i번째 원소를 끝으로 하는 최장 증가 부분 수열의 길이
inc_dp = [1] * n

# dec_dp[i] : i번째 원소를 시작으로 하는 최장 감소 부분 수열의 길이
dec_dp = [1] * n

# inc_dp 계산
for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

# dec_dp 계산
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if arr[j] < arr[i]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, inc_dp[i] + dec_dp[i] - 1)

print(ans)