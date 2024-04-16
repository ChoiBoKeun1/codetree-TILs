import sys

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def get_sum(x,y, w,h):
    cur = 0
    for i in range(x, x+h +1):
        for j in range(y, y+w +1):
            cur += arr[i][j]
    
    return cur

ans = -sys.maxsize

# rectangle1의 왼쪽위 점 i,j
for i in range(n):
    for j in range(m):
        # rectangle1 가로,세로길이
        for w1 in range(m):
            for h1 in range(n):
                if i+h1 >= n or j+w1 >= m:
                    continue
                
                for k in range(n):
                    for l in range(m):
                        for w2 in range(m):
                            for h2 in range(n):
                                if k+h2 >= n or l+w2 >= m:
                                    continue
                                
                                if i+h1 < k or j+w1 < l:
                                    rectangle1 = get_sum(i,j,w1,h1)
                                    rectangle2 = get_sum(k,l,w2,h2)
                                    ans = max(ans, rectangle1+rectangle2)

print(ans)