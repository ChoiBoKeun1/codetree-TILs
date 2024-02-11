import sys

arr = list(map(int,input().split()))

ans = sys.maxsize

for i in range(6):
    for j in range(i+1,6):
        for k in range(6):
            for l in range(k+1,6):
                if k == i or k == j or l == i or l == j:
                    continue

                sum1 = arr[i] + arr[j]
                sum2 = arr[k] + arr[l]
                sum3 = sum(arr) - sum1 - sum2
                
                # 3팀의 차이들 중 가장 큰 차이 == 가장 큰팀 - 가장 작은 팀
                diff = abs(sum1 - sum2)
                diff = max(diff, abs(sum2 - sum3))
                diff = max(diff, abs(sum1 - sum3))

                ans = min(ans, diff)

print(ans)