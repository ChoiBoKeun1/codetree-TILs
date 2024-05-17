n = int(input())
lines = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

main_line = [0] * 1001

selected_line_idx = []

overlapped_lines = 0
ans = 0

def is_overlapped():
    for elem in main_line:
        if elem > 1:
            return True
    return False

def recursive(num):
    global overlapped_lines, ans

    if is_overlapped():
        ans = max(ans, overlapped_lines -1)        
        return        

    for i in range(0,n):
        selected_line_idx.append(i)
        draw_line(i)
        overlapped_lines += 1
        recursive(num +1)
        
        erase_line(i)
        overlapped_lines -= 1
        selected_line_idx.pop()

def draw_line(idx):
    x1,x2 = lines[idx]

    for i in range(x1, x2+1):
        main_line[i] += 1

def erase_line(idx):
    x1,x2 = lines[idx]

    for i in range(x1, x2+1):
        main_line[i] -= 1

recursive(0)
print(ans)