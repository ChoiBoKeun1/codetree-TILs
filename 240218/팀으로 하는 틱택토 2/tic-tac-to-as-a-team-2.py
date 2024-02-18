arr = [
    list(map(int,input()))
    for _ in range(3)
]

def checkRow(i,j):
    for row in arr:
        cnt,cnt2 = 0,0
        for elem in row:
            if elem == i:
                cnt += 1
            elif elem == j:
                cnt2 += 1
        if (cnt == 2 and cnt2 == 1) or (cnt == 1 and cnt2 == 2):
            return True
    return False

def checkCol(i,j):
    for k in range(3):
        cnt,cnt2 = 0,0
        for l in range(3):
            if arr[l][k] == i:
                cnt += 1
            elif arr[l][k] == j:
                cnt2 += 1
        if (cnt == 2 and cnt2 == 1) or (cnt == 1 and cnt2 == 2):
            return True
    return False

def checkDiagonal(i,j):
    cnt,cnt2 = 0,0
    for k in range(3):
        if arr[k][k] == i:
            cnt += 1
        elif arr[k][k] == j:
            cnt2 += 1
    if (cnt == 2 and cnt2 == 1) or (cnt == 1 and cnt2 == 2):
            return True
    return False

def checkDiagonalRev(i,j):
    cnt,cnt2 = 0,0
    for k in range(3):
        if arr[k][2-k] == i:
            cnt += 1
        elif arr[k][2-k] == j:
            cnt2 += 1
    if (cnt == 2 and cnt2 == 1) or (cnt == 1 and cnt2 == 2):
            return True
    return False

MAX_N = 9
ans = 0
for i in range(1, MAX_N+1):
    for j in range(i+1, MAX_N+1):
        if i == j:
            continue
        if checkCol(i,j) or checkRow(i,j) or checkDiagonal(i,j) or checkDiagonalRev(i,j):
            ans += 1
print(ans)