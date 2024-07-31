# 모듈로 연산을 위한 상수 정의
MOD = 10**9 + 7

# 입력 값 읽기
n_str = input().strip()

# 박수를 칠 횟수를 세기 위한 변수
count = 0

# 큰 숫자 n을 문자열로 받아 각 자리수를 분석
length = len(n_str)

# 각 자리수에서 박수를 칠 경우를 분석하기 위한 알고리즘
def count_claps_up_to(x_str):
    # 숫자를 문자로 받아서 자리수별로 박수를 칠 경우를 분석합니다
    # 이 예제는 매우 기본적인 접근으로, 더 정교한 알고리즘이 필요합니다
    x = int(x_str)
    claps = 0
    
    for i in range(1, x + 1):
        if i % 3 == 0:
            claps += 1
        elif any(d in str(i) for d in '369'):
            claps += 1
    
    return claps % MOD

# 박수를 칠 횟수를 계산
result = count_claps_up_to(n_str)

# 결과 출력
print(result)