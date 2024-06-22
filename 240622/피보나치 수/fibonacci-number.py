n = int(input())

# using recursive
'''def fibbo(n):
    if n == 1 or n == 2:
        return 1
    
    return fibbo(n-1) + fibbo(n-2)

print(fibbo(n))
'''
# using memoization
'''memo = [-1] * (n+1)
def fibbo(n):
    if memo[n] != -1:
        return memo[n]

    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fibbo(n-1) + fibbo(n-2)

    return memo[n]

print(fibbo(n))
'''
# using tabulation
MAX_NUM = 45
dp = [0 for _ in range(MAX_NUM + 1)]

dp[1] = dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])