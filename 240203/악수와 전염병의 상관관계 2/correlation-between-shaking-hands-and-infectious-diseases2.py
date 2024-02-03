N,K,P,T = map(int,input().split())

shakes = []
for _ in range(T):
    t,x,y = map(int,input().split())
    shakes.append((t,x,y))

shake_num = [0] * 101
infect = [False] * 101

infect[P] = True

shakes.sort(key=lambda x: x[0])

for shake in shakes:
    target1 = shakes[1]
    target2 = shakes[2]

    if infect[target1]:
        shake_num[target1] += 1
    if infect[target2]:
        shake_num[target2] += 1

    if shake_num[target1] < K and infect[target1]:
        infect[target2] = True
    if shake_num[target2] < K and infect[target2]:
        infect[target1] = True
    

for i in range(1, N+1):
    print(infect[i],end='')