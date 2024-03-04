n = int(input())
arr = list(map(int,input().split()))

sorted_arr = sorted(arr)

cnt = 0

while arr != sorted_arr:
    first_elem = arr[0]
    last_elem = arr[n-1]

    if first_elem < last_elem:
        arr = arr[1:n-1] + [first_elem] + [last_elem]
        cnt += 1
    else:
        arr = arr[1:n] + [first_elem]
        cnt += 1

print(cnt)