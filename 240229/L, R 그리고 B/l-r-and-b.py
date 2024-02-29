n = 10
arr = []

start_i,start_j = 0,0
end_i,end_j = 0,0
R_i,R_j = 0,0

for i in range(n):
    row = input()
    for j in range(n):
        if row[j] == 'B':
            end_i,end_j = i,j   
        elif row[j] == 'L':
            start_i,start_j = i,j  
        elif row[j] == 'R':
            R_i,R_j = i,j       
    arr.append(row)
    
ans = 0

# 시작 row == 도착 row
if start_i == end_i:
    # R도 같은 row에 있는 경우,
    # R이 시작점과 도착점 사이에 있는지 확인 필요
    if start_i == R_i:
        if (start_j < R_j and R_j < end_j) or \
           (end_j < R_j and R_j < start_j):
            ans = abs(start_j - end_j) - 1 + 2
        else:
            ans = max(ans, abs(start_j - end_j) - 1)
    # R은 다른 row에 있는 경우.
    else:
        ans = max(ans, abs(start_j - end_j) - 1)

# 시작 col == 도착 col
elif start_j == end_j:
    # R도 같은 col에 있는 경우,
    # R이 시작점과 도착점 사이에 있는지 확인 필요
    if start_j == R_j:
        if (start_i < R_i and R_i < end_i) or \
           (end_i < R_i and R_i < start_i):
            ans = abs(start_i - end_i) - 1 + 2
        else:
            ans = max(ans, abs(start_i - end_i) - 1)
    # R은 다른 col에 있는 경우.
    else:
        ans = max(ans, abs(start_i - end_i) - 1)

# 그 외의 경우는, R의 위치에 관계없이, 시작점과 도착점만 고려하면 된다.
else:
    ans = abs(start_i - end_i) + abs(start_j - end_j) - 1

print(ans)