n = int(input())
arr = list()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push_back':
        num = cmd[1]
        arr.append(int(num))
    elif cmd[0] == 'get':
        num = cmd[1]
        print(arr[int(num)-1])
    elif cmd[0] == 'size':
        print(len(arr))
    elif cmd[0] == 'pop_back':
        arr.pop()