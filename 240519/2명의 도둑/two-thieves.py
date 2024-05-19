n, m, c = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

selected_list = []

ans = 0

def is_duplicated(x1, y1, x2, y2):
    return x1 == x2 and not (y1 + m <= y2 or y2 + m <= y1)

def recursive(cnt):
    global ans

    if cnt == 2:
        ans = max(ans, check())
        return

    for x1 in range(n):
        for y1 in range(n - m + 1):
            selected_list.append((x1, y1))
            recursive(cnt + 1)
            selected_list.pop()

def check():
    x1, y1 = selected_list[0]
    x2, y2 = selected_list[1]

    if is_duplicated(x1, y1, x2, y2):
        return 0

    cost1 = getCost(x1, y1)
    cost2 = getCost(x2, y2)

    return cost1 + cost2

def getCost(x, y):
    weights = arr[x][y:y + m]
    n = len(weights)
    max_value = 0

    def backtrack(index, current_weight, current_value):
        nonlocal max_value
        if current_weight > c:
            return
        max_value = max(max_value, current_value)
        if index == n:
            return
        # 선택하지 않는 경우
        backtrack(index + 1, current_weight, current_value)
        # 선택하는 경우
        backtrack(index + 1, current_weight + weights[index], current_value + weights[index] ** 2)

    backtrack(0, 0, 0)
    return max_value

recursive(0)
print(ans)