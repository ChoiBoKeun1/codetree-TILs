n = int(input())

arr = []
ans = 0

def Print():
    for e in arr:
        print(e, end=' ')
    print()

def choose(cur_idx):  
    global ans

    if cur_idx == n:
        if is_beautiful():
            ans += 1
        return
 
    for i in range(1,5):
        arr.append(i)
        choose(cur_idx +1)
        arr.pop()

def is_beautiful():
    
    # 시작위치 i
    i = 0
    while i < n:
        # i번째 위치에서부터
        # 연속하여 arr[i]가 arr[i] 개수 만큼 나올수 없다면
        # False
        if i + arr[i] > n:
            return False
        
        # 연속하여 arr[i] 숫자가 arr[i]만큼 나오는지 확인
        # 하나라도 다른 숫자라면
        # False
        for j in range(i, i+arr[i]):
            if arr[i] != arr[j]:
                return False
        
        # 다음 위치
        i += arr[i]

    return True

choose(0)
print(ans)