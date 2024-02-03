class Shake:
    def __init__(self,t,x,y):
        self.time, self.person1, self.person2 = t,x,y 

N,K,P,T = map(int,input().split())

shakes = []
for _ in range(T):
    t,x,y = map(int,input().split())
    shakes.append(Shake(t,x,y))

shake_num = [0] * 101
infect = [0] * 101

infect[P] = 1

# 시간을 기준으로 오름차순 정렬
# 빠른 시간이 앞으로 온다
shakes.sort(key=lambda x: x.time)

for shake in shakes:
    target1 = shake.person1
    target2 = shake.person2

    # 감염된 사람이 악수를 몇번을 했는가
    if infect[target1]:
        shake_num[target1] += 1
    if infect[target2]:
        shake_num[target2] += 1

    # 감염된 사람의 악수 횟수가 K 이하 and 감염되었으면
    if shake_num[target1] <= K and infect[target1]:
        infect[target2] = 1
    if shake_num[target2] <= K and infect[target2]:
        infect[target1] = 1
    
for i in range(1, N+1):
    print(infect[i],end='')