import sys

n = int(input())
arr = list(map(int,input().split()))

# 2 5 7 9 10 15
# 정렬 후 숫자 작은 그룹 반, 큰 그룹 반으로 나눴을때
# 각 그룹에서 같은 idx끼리 묶는게 가장 최선이다.

myarr = sorted(arr)
s_arr = myarr[0:n]
b_arr = myarr[n:2*n]

differs = []
for i in range(n):
    differs.append(b_arr[i] - s_arr[i])

ans = sys.maxsize
for elem in differs:
    ans = min(ans, elem)

print(ans)