n, m, c = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

selected = []
max_val = 0

def find_max_sum(cur_idx, cur_weight, cur_val):
    global max_val

    if cur_idx == m:
        if cur_weight <= c:
            max_val = max(max_val, cur_val)
        return

    # selected[cur_idx] 선택하지 않을 시
    find_max_sum(cur_idx +1, cur_weight, cur_val)

    # selected[cur_idx] 선택시
    # 무게 : + selected[cur_idx]
    # 가치 : + selected[cur_idx] ** 2
    find_max_sum(cur_idx +1, cur_weight + selected[cur_idx], 
                 cur_val + selected[cur_idx] ** 2)

# (x,y) ~ (x, y+ m-1) 까지 숫자들 중에서 고른다
# 무게의 합이 c를 넘지 않으면서 얻을수 있는 최대 value를 반환
def find_max(x, y):
    global selected, max_val

    selected = arr[x][y:y + m]

    max_val = 0
    find_max_sum(0,0,0)
    return max_val

# 두 선분 [a,b], [c,d] 가 겹치는지 확인
def intersect(a,b,c,d):
    # 겹치지 않는 경우의 반대를 return.
    return not (b < c or d < a)

# 두 도둑의 위치가 올바른지 확인
def possible(x1,y1, x2,y2):
    # 범위가 격자를 벗어나는 경우 : False
    if y1 + m-1 >= n or y2 + m-1 >= n:
        return False

    # 두 훔칠 위치의 행이 다르다
    # 항상 겹치지 않다 : True
    if x1 != x2:
        return True

    # 두 구간이 겹친다 : False
    if intersect(y1, y1 + m-1, y2, y2 + m-1):
        return False

    # 그 외 (격자 안에 있고, 행은 같은데, 겹치지 않음)
    return True

# 첫번째 도둑 : (x1,y1) ~ (x1, y1 + m-1)
# 두번째 도둑 : (x2,y2) ~ (x2, y2 + m-1)
# 가능한 모든 위치 탐색
ans = max([
    find_max(x1,y1) + find_max(x2,y2)
    for x1 in range(n)
    for y1 in range(n)
    for x2 in range(n)
    for y2 in range(n)
    if possible(x1,y1,x2,y2)
])
print(ans)