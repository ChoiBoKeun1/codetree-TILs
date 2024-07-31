MOD = 10**9 + 7

# 메모이제이션을 위한 배열을 초기화합니다.
def initialize_memo(max_digits):
    return [[[[ -1 for _ in range(2)] for _ in range(2)] for _ in range(3)] for _ in range(max_digits)]

def dp(s, x, sum_mod, f, over, memo):
    if x == len(s):
        return (1 if f or sum_mod == 0 else 0)
    
    if memo[x][sum_mod][f][over] != -1:
        return memo[x][sum_mod][f][over]

    memo[x][sum_mod][f][over] = 0
    limit = int(s[x]) if over else 9
    
    for i in range(limit + 1):
        new_sum_mod = (sum_mod + i) % 3
        new_f = f or (i % 3 == 0 and i != 0)
        new_over = over and (i == limit)
        memo[x][sum_mod][f][over] = (memo[x][sum_mod][f][over] + dp(s, x + 1, new_sum_mod, new_f, new_over, memo)) % MOD

    return memo[x][sum_mod][f][over]

def count_claps(n):
    s = str(n)
    memo = initialize_memo(len(s))
    total_claps = dp(s, 0, 0, False, True, memo)
    
    return total_claps

# 입력 처리
import sys
input = sys.stdin.read
n = int(input().strip())

# 결과 출력
print(count_claps(n)-1)