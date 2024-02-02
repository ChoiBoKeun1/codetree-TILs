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