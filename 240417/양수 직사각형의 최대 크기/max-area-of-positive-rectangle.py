n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def is_positive_rect(x1,y1, x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if arr[i][j] <= 0:
                return False
    
    return True

def get_size(x1,y1, x2,y2):
    return (x2-x1+1) * (y2-y1+1)

ans = -1

for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                if is_positive_rect(i,j,k,l):
                    ans = max(ans,get_size(i,j,k,l))

print(ans)