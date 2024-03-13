n = int(input())
arr = [-1] + list(map(int,input().split()))

def heap_sort(n):
    for i in range(n // 2, 0, -1):
        heapify(n,i)
    
    for i in range(n, 1, -1):
        arr[1],arr[i] = arr[i],arr[1]
        heapify(i-1, 1)

def heapify(n, i):
    largest = i
    l,r = 2*i, 2*i+1

    if l <= n and arr[l] > arr[largest]:
        largest = l

    if r <= n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(n, largest)


heap_sort(n)

for i in range(1, n+1):
    print(arr[i], end=' ')