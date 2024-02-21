import sys

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

ans = sys.maxsize
# 가장 낮은 언덕의 높이 : i
for i in range(101):
    total_cost = 0
    for elem in arr:
        if i <= elem and elem <= i+17:
            continue
             
        if elem < i:
            cost = (i - elem)**2
        
        if elem > i+17:
            cost = (elem-i-17)**2

        total_cost += cost

    ans = min(ans,total_cost)
print(ans)