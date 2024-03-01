import sys

n = int(input())
arr = list(map(int,input().split()))

MAX_NUM = -1001
MIN_NUM = 1001
for elem in arr:
    MAX_NUM = max(MAX_NUM, elem)
    MIN_NUM = min(MIN_NUM, elem)

ans = 0
if n == 3 and 0 in arr:
    print(0)
    sys.exit()

# 모든 숫자가 음수 인 경우
# 1. 절댓값이 가장 작은거 3개 = 가장 큰 수 3개
# 2. 0 포함된 경우, 0이 최댓값
if MAX_NUM == 0:
    print(0)
    sys.exit()
elif MAX_NUM < 0:
    myarr = sorted(arr)
    ans = myarr[n-1] * myarr[n-2] * myarr[n-3]

# + + +. 가장큰거 3개
elif MIN_NUM > 0:
    myarr = sorted(arr)
    ans = myarr[n-1] * myarr[n-2] * myarr[n-3]
# + - -
# 절댓값이 가장 큰 음수 2개 + 가장 큰 양수 1개
else:
    myarr = sorted(arr)
    ans = myarr[0] * myarr[1] * myarr[-1]

print(ans)