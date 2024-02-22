x = int(input())

speed = 0
idx = 0
cnt = 0

while idx + 2*(speed+1) <= x:
    speed += 1
    idx += 2*speed
    cnt += 2
    print("중간체크", idx, cnt, speed)

if idx + speed + 1 < x: #최고 속도가 1번시
    idx += speed + 1
    cnt += 1
    speed += 1
    print("최고 속도 한번", idx, cnt, speed)
    

    
print(cnt if idx == x else cnt + 1) #idx가 x가 아니면 speed이하에서 한번 유지시켜야함