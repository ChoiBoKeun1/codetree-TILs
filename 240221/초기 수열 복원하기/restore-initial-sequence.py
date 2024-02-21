n = int(input())
arr = list(map(int,input().split()))

def generate_permutations(arr):
    n = len(arr)

    if n == 1:
        return [(arr[0],)]

    all_permutations = []

    for i in range(n):
        fixed_element = arr[i]
        rest = arr[:i] + arr[i+1:]

        rest_permutations = generate_permutations(rest)

        for perm in rest_permutations:
            all_permutations.append((fixed_element,) + perm)

    return all_permutations

init_arr = [i for i in range(1,n+1)]
possible_arrs = generate_permutations(init_arr)

for possible_arr in possible_arrs:
    new_arr = []
    for i in range(n-1):
        new_arr.append(possible_arr[i] + possible_arr[i+1])

    if arr == new_arr:
        for elem in possible_arr:
            print(elem, end=' ')
        break