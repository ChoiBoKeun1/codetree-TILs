x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

new_x1 = min(x1,a1)
new_y1 = min(y1,b1)
new_x2 = max(x2,a2)
new_y2 = max(y2,b2)

print((new_x2-new_x1)*(new_y2-new_y1))