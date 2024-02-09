MAX_NUM = 100

n = int(input())
arr = [0] * (MAX_NUM+1)

for _ in range(n):
    idx, c = map(str,input().split())
    arr[int(idx)] = c

ans = 0
for i in range(MAX_NUM+1):
    for j in range(i, MAX_NUM+1):
        num_g, num_h = 0,0
        
        # 사진에서 양쪽 끝에 있는 사람 idx
        left,right = 102,-1
        
        # arr[i] ~ arr[j] 까지
        # G, H  개수를 센다
        for k in range(i,j+1):
            if arr[k] == 'G':
                num_g += 1
                left = min(left,k)
                right = max(right,k)
            elif arr[k] == 'H':
                num_h += 1
                left = min(left,k)
                right = max(right,k)
        
        length = right - left

        # 이 구간에 G,H 모두 없으면 다음 구간으로 넘어간다.
        if num_g == 0 and num_h == 0:
            continue
        
        # G,H의 개수가 같으면 ok.
        if num_g == num_h:
            ans = max(ans,length)
        # G 또는 H 둘 중 하나만 있으면 ok
        elif num_g == 0 or num_h == 0:
            ans = max(ans,length)

print(ans)