a,b = map(int,input().split())

num = b

myList = [2,4,6,8]

for i in range(4):
    while num >= a:
        print('%d * %d = %d' % (num, myList[i], int(num*myList[i])), end='')
        num -= 1
        if num >= a:
            print(' / ', end='')
    print()
    num = b