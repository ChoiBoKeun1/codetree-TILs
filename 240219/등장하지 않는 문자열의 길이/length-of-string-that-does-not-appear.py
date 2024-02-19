import sys

n = int(input())
string = input()

check = [False] * (n+1)

# j 부분문자열 시작위치
for j in range(n):
    # i 부분문자열의 길이
    for i in range(1,n+1):
        if not check[i]:
            cnt = 0
            if j+i <= n:
                sub_str = string[j:j+i]

                # string을 순회하며 몇번 나오는지 세보기
                for k in range(n):
                    if k+i <= n:
                        if sub_str == string[k:k+i]:
                            cnt += 1
            
            # 2번이상 나온경우
            # 해당하는 문자열 길이는 정답 후보에서 제외한다.
            if cnt >= 2:
                check[i] = True
                continue
        
ans = 0
for i in range(1,n+1):
    if check[i]:
        ans += 1
    else:
        ans += 1
        break
print(ans)