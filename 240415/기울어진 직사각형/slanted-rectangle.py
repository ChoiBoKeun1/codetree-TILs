n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

dx = [-1,-1,1,1]
dy = [1,-1,-1,1]

# i,j 시작점
cur_i, cur_j = 0,0

ans = 0

for i in range(2,n):
    for j in range(1,n-1):
        cur_i, cur_j = i,j
        start_i,start_j = i,j
        cur_dir = 0
        sum_val = 0

        sum_val += arr[cur_i][cur_j]

        # 한바퀴 돌기
        while cur_dir <= 3:
            
            # cur_dir 방향으로 점 이동
            cur_i += dx[cur_dir]
            cur_j += dy[cur_dir]

            # 만약 중간에, 범위를 벗어나서 시작점으로 미리 돌아와 버린 경우
            # 이 경우는 올바른 기울어진 직사각형이 아니므로, 고려하지 않기
            if start_i == cur_i and start_j == cur_j:
                break

            # 그 움직인 점이 범위를 벗어난 경우
            if not in_range(cur_i, cur_j):
                cur_i -= dx[cur_dir] # 범위 벗어나기 직전으로 점을 돌리고
                cur_j -= dy[cur_dir]
        
                cur_dir += 1         # 방향을 바꿔준다
                continue

            # 범위를 벗어나지 않은 경우, 합을 갱신한다.
            sum_val += arr[cur_i][cur_j]

        ans = max(ans, sum_val)

print(ans)