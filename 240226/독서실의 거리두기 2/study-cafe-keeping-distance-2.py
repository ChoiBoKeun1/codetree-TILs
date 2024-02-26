n = int(input())
seat = list(input())


def getminDist():
    min_dist = n
    for i in range(n):
        for j in range(i+1,n):
            if seat[i] == '1' and seat[j] == '1':
                min_dist = min(min_dist, j-i)
    return min_dist

ans = 0
for i in range(n):
    if seat[i] == '0':
        seat[i] = '1'
        ans = max(ans,getminDist())
        seat[i] = '0'
print(ans)