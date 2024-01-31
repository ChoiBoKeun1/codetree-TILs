n = int(input())
arr = [0] + list(map(int,input().split()))

# 최대공약수
def gcd(a,b):
    if b == 0: 
        return a
    else: 
        return gcd(b, a % b)

# 최소공배수
def lcm(a,b):
    return (a * b) // gcd(a,b)

# index번째 까지 인덱스의 숫자중에 가장 큰 값
def get_lcm_all(index):
    if index == 1:
        return arr[1]

    # 현재 index 숫자와
    # 1 ~ index-1 까지의 최소공배수를 구한 결과
    # 두 숫자의 최소공배수 구한다
    return lcm(get_lcm_all(index-1), arr[index])

print(get_lcm_all(n))