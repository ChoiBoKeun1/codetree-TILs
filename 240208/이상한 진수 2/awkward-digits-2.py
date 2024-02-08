a = input()
max_val = 0

number = a[:]
for i in range(len(number)-1):
    number = a[:]
    if number[i] == '0':
        number = number[:i] + '1' + number[i+1:]
    elif number[i] == '1':
        number = number[:i] + '0' + number[i+1:]

    max_val = max(max_val, int(number))

print(int(str(max_val),2))