MAX_t = 250
N,K,P,T = map(int,input().split())

meet = [(0,0)] * (MAX_t+1)

infect = [0] * 101

max_t = 0
for _ in range(T):
    t,x,y = map(int,input().split())
    
    # t초에 x개발자, y개발자 만남
    meet[t] = (x,y)

    max_t = max(max_t,t)


infect[P] = 1

for i in range(1, max_t+1):
    if K > 0:
        if P in meet[i]:
            other_value = meet[i][0] if meet[i][1] == P else meet[i][1]
            infect[other_value] = 1
            K -= 1        

for i in range(1, N+1):
    print(infect[i],end='')