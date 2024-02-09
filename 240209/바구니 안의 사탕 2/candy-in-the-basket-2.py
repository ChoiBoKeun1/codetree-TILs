n,k = map(int,input().split())

MAX_IDX = 100 + 2*k + 1

arr = [0] * MAX_IDX
for _ in range(n):
    num, idx = map(int,input().split())
    arr[idx] += num

'''
[c-K, c+K]
[0, 2K] 
길이 : 2K + 1
'''

ans = 0
# i는 시작점 idx
for i in range(MAX_IDX - 2*k):
    sum_val = 0
    for l in range(i, i+2*k + 1):
        sum_val += arr[l]
    ans = max(ans,sum_val)

print(ans)