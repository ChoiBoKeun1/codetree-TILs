n,m,c = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

selected_list = []

ans = 0

def is_duplicated(x1,y1, x2,y2):
    return x1 == x2 and ((y1 <= y2 <= y1 +m-1) or (y2 <= y1 <= y2 +m-1)) 

def recursive(cnt):
    global ans

    if cnt == 2:
        ans = max(ans,check())
        return


    for x1 in range(n):
        for y1 in range(n):
            selected_list.append((x1,y1))
            recursive(cnt +1)
            selected_list.pop()

def check():
    x1,y1 = selected_list[0]
    x2,y2 = selected_list[1]

    if is_duplicated(x1,y1, x2,y2):
        return 0

    theif1 = arr[x1][y1:y1+m]
    theif1.sort(reverse=True)

    theif2 = arr[x2][y2:y2+m]
    theif2.sort(reverse=True)

    weight1 = 0
    cost1 = 0
    for elem in theif1:
        weight1 += elem
        if weight1 > c:
            weight1 -= elem
            break
        else:
            cost1 += elem*elem

    weight2 = 0
    cost2 = 0
    for elem in theif2:
        weight2 += elem
        if weight2 > c:
            weight2 -= elem
            break
        else:
            cost2 += elem*elem

    return cost1 + cost2

recursive(0)
print(ans)