n = int(input())
arr = list(map(int,input().split()))

# 수열이 어느 idx부터 정렬되어있는지를 확인
# 앞부분에서 정렬되어있지 않은 원소들의 개수가 정답

# 수열의 뒤에서부터 확인하면서, 어디까지 정렬되어있는지를 확인

idx = n-2
# idx 가 0보다 크고, 정렬이 되어있는지를 확인한다
while idx >= 0 and arr[idx] < arr[idx+1]:
    idx -= 1

# while문 탈출시, idx+1 개의 원소가 정렬되어있지 않다는 뜻이다.
print(idx+1)