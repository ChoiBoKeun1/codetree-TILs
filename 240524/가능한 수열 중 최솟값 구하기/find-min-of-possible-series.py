import sys

n = int(input())

arr = []

def is_possible():
    length = 1
    while True:
        start1,end1 = len(arr) - length, len(arr) - 1
        start2,end2 = start1 - length, start1 - 1

        if start2 < 0:
            break

        if arr[start1 : end1 +1] == arr[start2 : end2 +1]:
            return False

        length += 1
    
    return True

def find_min_arr(cnt):
    if cnt == n: 
        for elem in arr:
            print(arr, end='')
        sys.exit(0)

    for number in numbers:
        arr.append(number)
        if is_possible():
            find_min_arr(cnt+1)
        arr.pop()

find_min_arr(0)