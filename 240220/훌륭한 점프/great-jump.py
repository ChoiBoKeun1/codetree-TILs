MAX_NUM = 100
n,k = map(int,input().split())
arr = list(map(int,input().split()))

# 마지막 index로 부터
# 숫자 limit를 넘지 않으면서
# 거리 k 이내로 계속 이동이 가능한가?
def is_possible(limit):
    last_idx = 0
    for i in range(1,n):
        if arr[i] <= limit:
            if i - last_idx > k:
                return False
            last_idx = i
    
    return True

# 밟으며 지나간 최댓값을 i라고 했을때
# 거리 k 이내로 점프하며 끝까지 도달하는 게 가능한가?
# 가능하면, 그때 i가 최솟값.
miniMax = MAX_NUM + 1
for i in range(max(arr[0],arr[-1]), MAX_NUM+1):
    if is_possible(i):
        print(i)
        break