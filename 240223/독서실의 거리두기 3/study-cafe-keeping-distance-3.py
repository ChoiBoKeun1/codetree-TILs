n = int(input())
seat = list(input())

# 현 상태에서, 가장 가까운 두사람들 중에서, 가장 멀리 떨어져있는 경우를 찾는다
p1,p2 = -1,-1
dist = 0
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == '1' and seat[j] == '1':
            if j-i > dist:
                dist = j-i
                p1,p2 = i,j
            break

# 두 자리 p1,p2 사이 가운데에 새로운 1을 넣는다
seat[(p1+p2) // 2] = '1'

# 새로 만들어진 seat에서, 가장 가까운 두사람들 중에서, 가장 멀리 떨어져있는 경우를 찾는다
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == '1' and seat[j] == '1':
            if j-i < dist:
                dist = j-i
            break
print(dist)