n = int(input())
h = [
    int(input())
    for _ in range(n)
]

ans = 0
# i : 해수면 높이
for i in range(1,1001):
    cnt = 0

    # 가장 왼쪽에 빙산이 있으면 추가. 
    if h[0] > i:
        cnt += 1

    # j-1번째 빙산은 잠기고
    # j번째 빙산은 떠있으면
    # j번째부터 시작하는 빙산이 있다.
    for j in range(1,n):
        if h[j] > i and h[j-1] <= i:
            cnt += 1
    
    ans = max(ans,cnt)

print(ans)