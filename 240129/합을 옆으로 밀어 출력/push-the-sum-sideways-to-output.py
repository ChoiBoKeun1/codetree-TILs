n = int(input())

sum = 0

for _ in range(n):
    sum += int(input())

string = str(sum)

string = string[1:] + string[0]
print(string)