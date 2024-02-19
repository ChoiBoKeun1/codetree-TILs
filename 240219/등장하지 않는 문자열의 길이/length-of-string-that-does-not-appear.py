import sys

n = int(input())
string = input()

ans_str_len = sys.maxsize

# i 부분문자열의 길이
for i in range(1,n+1):
    cnt = 0
    # j 부분문자열 시작위치
    for j in range(n):
        if j+i <= n:
            sub_str = string[j:j+i]
            
            # string을 순회하며 몇번 나오는지 세보기
            for k in range(n):
                if k+i <= n:
                    if sub_str == string[k:k+i]:
                        cnt += 1
        if cnt < 2:
            ans_str_len = min(ans_str_len,i)

print(ans_str_len)