n,t = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = list(map(int,input().split()))

def print_list(arr):
    for elem in arr:
        print(elem, end=' ')
    print()

for _ in range(t):
    tmp1 = arr1[n-1]
    tmp2 = arr2[n-1]
    tmp3 = arr3[n-1]
    for i in range(n-1, 0, -1):
        arr1[i] = arr1[i-1]
        arr2[i] = arr2[i-1]
        arr3[i] = arr3[i-1]

    arr2[0] = tmp1
    arr3[0] = tmp2
    arr1[0] = tmp3

print_list(arr1)
print_list(arr2)
print_list(arr3)