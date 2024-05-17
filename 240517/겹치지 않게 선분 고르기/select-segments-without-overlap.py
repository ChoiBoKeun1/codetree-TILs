n = int(input())
lines = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

selected_lines = []
ans = 0

# 선분 2개가 겹치는지 확인
def overlapped(line1, line2):
    ax1,ax2 = line1
    bx1,bx2 = line2

    # 한 점이 다른 선분에 포함되는 경우, 겹친다고 판단할 수 있다.
    return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
           (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)

# 단 한쌍이라도 겹치면 안된다.
def possible():
    for i, line1 in enumerate(selected_lines):
        for j, line2 in enumerate(selected_lines):
            if i != j and overlapped(line1, line2):
                return False
    return True    

def recursive(cnt):
    global ans

    if cnt == n:
        if possible():
            ans = max(ans, len(selected_lines))
        
        return
    
    # cnt번째 선분을 선택
    selected_lines.append(lines[cnt])
    recursive(cnt +1)
    selected_lines.pop()

    # cnt번째 선분은 선택하지 않고, cnt+1 번째 선분을 선택
    recursive(cnt +1)
    
recursive(0)
print(ans)