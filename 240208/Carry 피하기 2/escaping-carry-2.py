n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

def isCarry(n1,n2):
    while n1 > 0 and n2 > 0:
        a = n1 % 10
        b = n2 % 10
        if a+b >= 10:
            return True
        n1,n2 = n1 // 10, n2 // 10
    return False
        
ans = -1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if not isCarry(arr[i],arr[j]):
                sum_val = arr[i] + arr[j]
                if not isCarry(sum_val, arr[k]):
                    sum_val += arr[k]
                    ans = max(ans,sum_val)

print(ans)