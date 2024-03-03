n = int(input())
arr = list(map(int,input().split()))

even,odd = 0,0
cnt = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

for i in range(n):
    # 이 묶음의 합이 짝수여야 한다.
    if cnt % 2 == 0:
        # 사용할 짝수가 남아있는 경우
        if even:
            even -= 1
            cnt += 1
        # 짝수 없음. 홀수만으로 만들어야 한다
        else:
            # 2개 이상의 홀수가 존재할때
            if odd >= 2:
                odd -= 2
                cnt += 1
            else:
                # 아직 값이 남아있을 때
                if odd > 0:
                    cnt -= 1
                break
    # 이 묶음의 합이 홀수여야 한다.
    else:
        # 사용할 홀수가 남아있는 경우
        if odd:
            odd -= 1
            cnt += 1
        else:
            break

print(cnt)