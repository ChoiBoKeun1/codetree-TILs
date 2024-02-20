MAX_NUM = 10000

n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

# 최대값 최솟값 차이가 K 이하가 되야 한다
# -> 선택한 숫자들이 i <= 숫자들 <= i+k 이 되야한다.
# -> 가능한 모든 i를 찾는다

ans = 0
for i in range(1,MAX_NUM+1):
    cnt = 0
    for elem in arr:
        if i <= elem and elem <= i+k:
            cnt += 1
    
    ans = max(ans,cnt)

print(ans)