import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int,input().split()))

list1, list2 = list(), list()

all_sum = sum(arr)

ans = INT_MAX

def make_list(start, cnt):
    global ans
    
    if cnt == n:
        sum1 = sum(list1)
        sum2 = all_sum - sum1
        ans = min(ans, abs(sum1-sum2))
        return

    for i in range(start, 2*n):
        list1.append(arr[i])
        make_list(start +i, cnt +1)
        list1.pop()


make_list(0,0)
print(ans)