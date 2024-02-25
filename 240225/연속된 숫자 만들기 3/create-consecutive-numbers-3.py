arr = list(map(int,input().split()))
arr.sort()

# 처음부터 연속된 경우
ans = 0
if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
        ans = 0
else:
    left_dist = arr[1]-arr[0]
    right_dist = arr[2]-arr[1]

    ans = abs(right_dist - left_dist)


'''
1 2 10
2 9 10  1
2 3 9   2
3 8 9   3
3 4 8   4
4 7 8   5
4 5 7   6
5 6 7   7

'''

print(ans)