from itertools import permutations

n = int(input())
arr = list(map(int,input().split()))


init_arr = [i for i in range(1,n+1)]
all_permutations = permutations(init_arr)
possible_arrs = list(all_permutations)

for possible_arr in possible_arrs:
    new_arr = []
    for i in range(n-1):
        new_arr.append(possible_arr[i] + possible_arr[i+1])

    if arr == new_arr:
        for elem in possible_arr:
            print(elem, end=' ')
        break