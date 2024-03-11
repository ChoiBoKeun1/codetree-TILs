# 1 <= 원소 값 <= 100000 이므로, 최대 자릿수 개수는 6
MAX_K = 6

# 숫자니까 0 ~ 9 10개.
MAX_DIGIT = 10

n = int(input())
arr = list(map(int,input().split()))

def radix_sort():
    global arr

    p = 1
    for pos in range(MAX_K):
        new_arr = [ [] for _ in range(MAX_DIGIT) ]

        for elem in arr:
            digit = (elem // p) % 10
            new_arr[digit].append(elem)

        arr = []
        for i in range(MAX_DIGIT):
            for j in range(len(new_arr[i])):
                arr.append(new_arr[i][j])

        p *= 10

radix_sort()

for e in arr:
    print(e, end=' ')