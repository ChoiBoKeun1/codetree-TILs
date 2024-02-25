arr = list(map(int,input().split()))
arr.sort()

def isAnswer():
    if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
        return True
    return False


# 처음부터 연속된 경우
ans = 0
while not isAnswer():
    left_dist = arr[1]-arr[0]
    right_dist = arr[2]-arr[1]

    if left_dist <= right_dist:
        arr[0] = arr[2]-1
    else:
        arr[2] = arr[0]+1
    ans += 1
    arr.sort()
    
print(ans)