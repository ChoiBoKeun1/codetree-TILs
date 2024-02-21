n = int(input())
arr = list(map(int,input().split()))

sequence = [0]*n

# 첫번째 원소를 i라 가정
for i in range(1,n+1):
    sequence[0] = i
    
    for j in range(n-1):
        next_val = arr[j] - sequence[j]
        if next_val > 0 and next_val <= n:
            sequence[j+1] = next_val
        else:
            break
    
    # sequence의 모든 원소가 유일한가
    if len(sequence) == len(set(sequence)) and len(sequence) == n:
        new_sum_arr = []
        for j in range(n-1):
            new_sum_arr.append(sequence[j]+sequence[j+1])
        
        if arr == new_sum_arr:
            for elem in sequence:
                print(elem, end=' ')