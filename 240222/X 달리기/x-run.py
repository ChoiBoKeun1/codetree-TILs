x = int(input())

cur_speed = 1
time = 0
dist = 0

while time < x:
    dist += cur_speed
    time += 1
    
    if dist < x/2:
        cur_speed += 1
    elif dist >= x/2 and cur_speed > 1:
        cur_speed -= 1

    if dist == x:
        break
    
print(time)