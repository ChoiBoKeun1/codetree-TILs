n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer_list = []

for i in range(n):
    # i번째 row에서, 1*3 격자 내 최대값
    max_val_row = 0
    max_i, max_j = -1,-1
    for j in range(n-2):
        sum_val = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        if max_val_row < sum_val:
            max_val_row = sum_val
            max_i,max_j = i,j

    # i번째 row에서, 1*3 격자 내
    # 그 다음으로 큰 값(존재한다면)
    max_val_row2 = 0
    for j in range(n-2):
        if max_j <= j and j <= max_j+2:
            continue
        sum_val = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        if max_val_row2 < sum_val:
            max_val_row2 = sum_val

    answer_list.append(max_val_row)
    answer_list.append(max_val_row2)

sorted_list = sorted(answer_list)
sorted_list.reverse()
print(sorted_list[0] + sorted_list[1])