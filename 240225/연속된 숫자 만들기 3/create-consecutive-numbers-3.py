arr = list(map(int,input().split()))
arr.sort()

# 처음부터 연속된 경우
ans = 0
if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
        ans = 0
else:
    left_dist = arr[1] - arr[0]
    right_dist = arr[2] - arr[1]

    ans = max(left_dist, right_dist)-1

'''
1 2 10. left_dist = 1, right_dist = 8
2 9 10  1
2 3 9   2
3 8 9   3
3 4 8   4
4 7 8   5
4 5 7   6
5 6 7   7

4 7 14. left_dist = 3, right_dist = 7
7 13 14  1
7 8 13   2
8 12 13  3
8 9 12   4
9 11 12  5
9 10 12  6
'''

print(ans)