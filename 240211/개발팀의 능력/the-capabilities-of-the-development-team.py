import sys

arr = list(map(int,input().split()))
n = 5

ans = sys.maxsize
hasAnswer = False
for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            for l in range(k+1, n):
                if k == i or k == j or l == i or l == j:
                    continue
                
                sum1 = arr[i] + arr[j]
                sum2 = arr[k] + arr[l]
                sum3 = sum(arr) - sum1 - sum2

                if sum1 == sum2 or sum1 == sum3 or sum2 == sum3:
                    continue
                else:
                    hasAnswer = True
                    diff = abs(sum1 - sum2)
                    diff = max(diff, abs(sum2 - sum3))
                    diff = max(diff, abs(sum1 - sum3))
                    ans = min(ans, diff)

if not hasAnswer:
    ans = -1

print(ans)