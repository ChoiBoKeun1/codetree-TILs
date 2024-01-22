a,b = map(int,input().split())

remainders = [0 for _ in range(b)]

while a > 1:
    # 나머지 구하기
    remainder = a % b
    # 해당 idx에 +1
    remainders[remainder] += 1
    
    a = int(a / b)

result = 0

for re in remainders:
    result += re**2

print(result)