import sys

INT_MAX = sys.maxsize
MAX_R = 100

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
dp = [
    [0] * n
    for _ in range(n)
]

ans = INT_MAX

def initialize():
    # dp를 INT_MAX로 초기화
    for i in range(n):
        for j in range(n):
            dp[i][j] = INT_MAX

    # 시작점 초기화
    dp[0][0] = arr[0][0]

    # 최좌측 열 초기값
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0], arr[i][0])

    # 최상단 행 초기값
    for j in range(1,n):
        dp[0][j] = max(dp[0][j-1], arr[0][j])

def solve(lower_bound):
    # lower_bound 미만의 값은 사용할 수 없도록
    # arr 값 변경
    for i in range(n):
        for j in range(n):
            if arr[i][j] < lower_bound:
                arr[i][j] = INT_MAX

    # dp 초기값 설정
    initialize()

    # 탐색하는 위치의 (위측, 좌측) 값 중 작은값과
    # 해당 위치의 숫자 중에 최댓값을 구한다
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), arr[i][j])

    return dp[n-1][n-1]

# main
# 최솟값을 k 라고 가정했을 때 (최솟값 고정)
# lower_bound 이상의 수들만 사용하여
# 이동한다는 조건하에서
# 최댓값을 최소로 만드는 dp 문제
for lower_bound in range(1, MAX_R +1):
    upper_bound = solve(lower_bound)

    # 다 진행했음에도 여전히 INT_MAX라면
    # 그런 이동이 불가능하다는 뜻 이므로
    # 패스
    if upper_bound == INT_MAX:
        continue

    # 답 갱신
    ans = min(ans, upper_bound - lower_bound)

print(ans)