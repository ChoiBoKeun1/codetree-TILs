import sys

n = int(input())
arr = list(map(int,input().split()))

ans = sys.maxsize
for i in range(n):
    # i번째 원소를 2배 한다.
    arr[i] *= 2

    # j번째 원소 빼고, 나머지 list.
    for j in range(n):
        tmp_list = []
        
        for k in range(n):
            if j != k:
                tmp_list.append(arr[k])
        
        sum_diff = 0
        for k in range(n-2):
            sum_diff += abs(tmp_list[k] - tmp_list[k+1])
        ans = min(sum_diff,ans)

    arr[i] //= 2

print(ans)