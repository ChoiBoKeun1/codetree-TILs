n = int(input())

MOD = 10007

def count_ways_recursive(n, memo=None):
    if memo is None:
        memo = {}
        
    # 기본 케이스
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    # 메모이제이션 확인
    if n in memo:
        return memo[n]
    
    # 1, 2, 5를 사용하여 재귀적으로 방법의 수를 계산
    memo[n] = count_ways_recursive(n - 1, memo) + count_ways_recursive(n - 2, memo) + count_ways_recursive(n - 5, memo)
    return memo[n]

print(count_ways_recursive(n) % 10007)