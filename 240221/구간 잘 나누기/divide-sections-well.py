import sys

n,m = map(int,input().split())
arr = list(map(int,input().split()))

def calculate_max_sum(barriers):
    partitions = []
    
    # 초기 칸막이 위치 설정
    barriers = [0] + [barriers] + [len(arr) - 1]
    
    # 칸막이 위치에 따라 구간을 나누어 구간 합 계산
    for i in range(1, len(barriers) - m + 2):
        partition = arr[barriers[i - 1]:barriers[i]]
        partitions.append(sum(partition))
    
    return max(partitions)

ans = sys.maxsize

for barriers in range(1,n):
    if barriers >= m-1:
        max_part_sum = calculate_max_sum(barriers)
        ans = min(ans, max_part_sum)


print(ans)