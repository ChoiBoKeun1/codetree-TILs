n = int(input())

arr = []

def is_possible():
    length = len(arr)
    for i in range(1, length//2 + 1):
        if arr[-i:] == arr[-2*i:-i]:
            return False
    return True

def find_max(cnt):
    global arr

    if cnt == n: 
        return arr

    for i in range(4, 6+1):
        arr.append(i)
        if is_possible():
            result = find_max(cnt+1)
            if result:
                return result
        arr.pop()
        
    return None

for elem in find_max(0):
    print(elem,end='')