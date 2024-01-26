n = int(input())

arr = []

for i in range(n):
    arr.append(input())

condition = input()

cnt = 0
length = 0

for elem in arr:
    if elem[0] == condition:
        cnt += 1
        length += len(elem)

print("%d %.2f" % (cnt,length/cnt))