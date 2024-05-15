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

    else:
        for i in range(1,5):
            arr.append(i)
            choose(cur_idx +1)
            arr.pop()

def is_beautiful():
    i = 0
    while i < n:
        if i + arr[i] - 1 >= n:
            return False
        
        for j in range(i, i+arr[i]):
            if arr[i] != arr[j]:
                return False
        i += arr[i]

    return True
    
choose(0)
print(ans)