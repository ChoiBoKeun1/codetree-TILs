n = int(input())
arr = [0] + [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(1,4):
    point = 0

    stone = [0] * 4
    stone[i] = 1

    for j in range(1,4):
        a,b,c = arr[j]
        stone[a],stone[b] = stone[b],stone[a]
        if stone[c]:
            point += 1
    ans = max(ans,point)
print(ans)