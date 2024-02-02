'''
a,b = map(int,input().split())
n = int(input())

def a_to_decimal(a,n):
    number = 0
    cnt = 0
    while n // 10 != 0:
        number += (n % 10) * (a ** cnt)
        cnt += 1
        n //= 10
    number += n * (a**cnt)

    return number



def decimal_to_b(b,n):
    number = 0
    cnt = 0
    while n // b != 0:
        number += (n % b) * (10 ** cnt)
        cnt += 1
        n //= b
    number += n * (10**cnt)

    return number

decimal = a_to_decimal(a,n)
answer = decimal_to_b(b,decimal)

print(answer)

'''
a,b = map(int,input().split())
n = input()

digits = []

# 10진수로 변환
num = 0
for ch in n:
    num = num * a + (int(ch))

# b진수로 변환
while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

# 진수 배열을 뒤집어 b진수 출력
for digit in digits[::-1]:
    print(digit, end='')