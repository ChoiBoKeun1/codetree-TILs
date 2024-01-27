A = input()
B = input()

AB = A + B
BA = B + A

if AB[0]==BA[0] and AB[1]==BA[1]:
    print('true')
else:
    print('false')