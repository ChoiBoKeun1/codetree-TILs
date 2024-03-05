import sys

n = int(input())
arr = list(map(int,input().split()))

# 정렬 후 숫자 작은 그룹 반, 큰 그룹 반으로 나눴을때
# 각 그룹에서 같은 idx끼리 묶는게 가장 최선이다.
# 즉 arr[0] 과 arr[0+n] 을 묶는것이다

arr.sort()

ans = sys.maxsize
for i in range(n):
    ans = min(ans, arr[n+i]-arr[i])

print(ans)