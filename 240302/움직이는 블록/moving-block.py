n = int(input())
arr = [ int(input()) for _ in range(n) ]

final_val = sum(arr) // n

ans = 0
for elem in arr:
    if elem < final_val:
        ans += abs(elem-final_val)

print(ans)