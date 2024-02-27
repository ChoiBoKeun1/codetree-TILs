n = int(input())
arr = list(input().split())

cnt = 0

for i in range(n):
    # i번째 알파벳 x 선언.
    x = chr(ord('A') + i)

    # x 의 현재 idx를 찾는다
    idx = 0
    for j in range(n):
        if arr[j] == x:
            idx = j

    # x를 i로 옮긴다.
    for j in range(idx-1, i-1, -1):
        arr[j],arr[j+1] = arr[j+1],arr[j]
        cnt += 1

print(cnt)