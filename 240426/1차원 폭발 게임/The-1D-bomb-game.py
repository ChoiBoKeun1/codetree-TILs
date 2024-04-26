n,m = map(int,input().split())
arr = [
    int(input())
    for _ in range(n)
]

# 시작 idx와, 그 값(cur_num == arr[start_idx]) 이 주어졌을 때,
# 끝 idx를 구하는 함수
def get_end_idx(start_idx, cur_num):
    for i in range(start_idx+1, len(arr)):
        if arr[i] != cur_num:
            return i-1
    
    # 시작idx ~ arr 끝까지 같은 값인 경우이다.
    return len(arr)-1

# 계속 반복
while True:
    did_explode = False
    cur_idx = 0

    # 현재 idx부터 arr 끝까지
    while cur_idx < len(arr):
        # 현재 idx 값에 대한 끝 idx 구한다
        end_idx = get_end_idx(cur_idx, arr[cur_idx])

        # end - cur + 1 == 연속한 폭탄의 개수
        # 연속한 폭탄 개수가 m보다 크거나 같으면, 폭발
        if end_idx - cur_idx + 1 >= m:
            del arr[cur_idx : end_idx+1]
            did_explode = True
        
        # arr[cur_idx] 폭탄이 터질수 없는 경우
        # 그 다음 idx 폭탄에 대해 탐색을 진행
        else:
            cur_idx = end_idx+1

    # 모든 idx 순회가 끝난 후
    # 폭발한 적이 없는 경우
    # while문을 종료시킨다.
    if not did_explode:
        break

    # 만약 폭발이 한번이라도 있다면,
    # arr가 폭발에 의해 형태가 변경이 되어
    # 또 폭발할 경우를 고려해야 하기 때문이다.
    # ex) m = 2, arr = [1 2 2 1] -> 2 2 폭발 -> [1 1] 
    #     이 경우 1 1이 또 폭발 해야 한다.

print(len(arr))
for elem in arr:
    print(elem)