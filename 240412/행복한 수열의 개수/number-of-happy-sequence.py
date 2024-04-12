n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
ans = 0

def isHappy(arr):
    global ans

    for i in range(n-m+1):
        if arr[i:i+m].count(arr[i]) >= m:
            ans += 1
            break


for row in range(n):
    isHappy(arr[row])

for col in range(n):
    new_arr = []
    for row in range(n):
        new_arr.append(arr[row][col])
    
    isHappy(new_arr)


print(ans)