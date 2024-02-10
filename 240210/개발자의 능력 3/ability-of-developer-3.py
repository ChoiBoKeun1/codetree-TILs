import sys

arr = list(map(int,input().split()))
length = len(arr)

total_sum = sum(arr)

ans = sys.maxsize
for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            team1 = arr[i] + arr[j] + arr[k]
            team2 = total_sum - team1
            ans = min(ans, abs(team1-team2))

print(ans)