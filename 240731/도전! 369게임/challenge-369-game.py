MOD = 10**9 + 7

# 입력
n = int(input())

# 박수 횟수를 세기 위한 변수
count = 0

# 1부터 n까지 반복
for i in range(1, n + 1):
    # 현재 숫자 i가 3의 배수일 경우
    if i % 3 == 0:
        count += 1
    else:
        # 숫자 i에 3, 6, 9가 포함되어 있는지 확인
        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            count += 1

# 결과를 MOD로 나눈 나머지로 계산
result = count % MOD

# 결과 출력
print(result)