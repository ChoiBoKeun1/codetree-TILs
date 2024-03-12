n = int(input())
arr = list(map(int,input().split()))
merged_arr = [0] * n

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid+1, high)
        merge(low, mid, high)

def merge(low, mid, high):
    i, j = low, mid + 1
    
    k = low
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            merged_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        merged_arr[k] = arr[i]
        i += 1

    while j <= high:
        merged_arr[k] = arr[j]
        j += 1

    for k in range(low, high+1):
        arr[k] = merged_arr[k]
    

merge_sort(0,n-1)

for e in arr:
    print(e, end=' ')