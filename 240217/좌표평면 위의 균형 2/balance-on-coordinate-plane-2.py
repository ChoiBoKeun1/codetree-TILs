MAX_X = 100
n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 101
for i in range(2,MAX_X+1,2):
    for j in range(2,MAX_X+1,2):
        
        area1,area2,area3,area4 = 0,0,0,0
        for x,y in arr:
            if x > i and y > j:
                area1 += 1
            elif x < i and y > j:
                area2 += 1
            elif x < i and y < j:
                area3 += 1
            elif x > i and y < j:
                area4 += 1
        M = max(area1,area2,area3,area4)
        ans = min(ans,M)
print(ans)