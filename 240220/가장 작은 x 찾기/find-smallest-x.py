n = int(input())
a_list, b_list = [0],[0]

for _ in range(n):
    a,b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)

ans = 10001
for i in range(1,10001):
    isPossible = True
    for j in range(1,n+1):
        val = i * (2**j)
        if a_list[j] <= val and val <= b_list[j]:
            continue
        else:
            isPossible = False
            break   
    if isPossible:
        ans = min(ans,i)
print(ans)