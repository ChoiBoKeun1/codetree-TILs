n = int(input())

numbers = list(map(int,input().split()))


for number in reversed(numbers):
    if number % 2 == 0:
        print(number, end=' ')