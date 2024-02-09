from itertools import permutations

n,m = map(int,input().split())
arr_A = list(map(int,input().split()))
arr_B = list(map(int,input().split()))

ans = 0
if n < m:
    print(ans)
else:
    all_permutations = list(permutations(arr_B))
    beautiful_lists = [list(perm) for perm in all_permutations]


    for i in range(n-m+1):
        if arr_A[i:i+m] in beautiful_lists:
            ans += 1
    print(ans)