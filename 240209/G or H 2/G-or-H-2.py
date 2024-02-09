MAX_NUM = 100

n = int(input())
arr = [0] * (MAX_NUM+1)

for _ in range(n):
    idx, c = map(str,input().split())
    arr[int(idx)] = c

ans = 0
for i in range(MAX_NUM+1):
    for j in range(i, MAX_NUM+1):
        # 해당 위치에 사람이 없으면 skip
        if arr[i] == 0 or arr[j] == 0:
            continue

        num_g, num_h = 0,0
        
        # arr[i] ~ arr[j] 까지
        # G, H  개수를 센다
        for k in range(i,j+1):
            if arr[k] == 'G':
                num_g += 1
            elif arr[k] == 'H':
                num_h += 1

        # G 또는 H 둘 중 하나만 있거나
        # G, H 개수가 같다면
        if num_g == 0 or num_h == 0 or num_g == num_h:
            length = j-i
            ans = max(ans,length)

print(ans)