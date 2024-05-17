n = int(input())
lines = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

selected_lines = []
ans = 0

def is_overlapped():
    for idx1,v1 in enumerate(selected_lines):
        for idx2,v2 in enumerate(selected_lines):
            x1,y1 = v1
            x2,y2 = v2

            if idx1 != idx2:
                if x1 <= x2 <= y1 or x1 <= y2 <= y1 or \
                    x2 <= x1 < y2 or x2 <= y1 <= y2:
                    return False
    
    return True

def recursive(cnt):
    global ans

    if cnt == n:
        if is_overlapped():
            ans = max(ans, len(selected_lines))
        
        return
    
    selected_lines.append(lines[cnt])
    recursive(cnt +1)
    selected_lines.pop()

    recursive(cnt +1)

recursive(0)
print(ans)