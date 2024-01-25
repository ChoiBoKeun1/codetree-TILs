strlist = []

min_val = 21
max_val = 0

for _ in range(3):
    strlist.append(input())

for i in range(3):
    min_val = min(len(strlist[i]),min_val)
    max_val = max(len(strlist[i]),max_val)

print(max_val-min_val)