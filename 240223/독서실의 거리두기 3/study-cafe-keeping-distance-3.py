n = int(input())
seat = list(input())

def get_minDiff():
    cnt = 0
    arr = []
    for i in range(n):
        if seat[i] == '1':
            arr.append(cnt)
            cnt = 0
        cnt += 1

    return min(arr[1:])

ans = -1
for i in range(n):
    if seat[i] == '0':
        seat[i] = '1'
        ans = max(get_minDiff(),ans)
        seat[i] = 0

print(ans)