n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

total_dist = 0
for i in range(n-1):
    move_right = max(0, a[i]-b[i])
    a[i+1] += move_right
    total_dist += move_right

print(total_dist)