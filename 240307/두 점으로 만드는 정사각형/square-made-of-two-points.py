x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

width = max(x2,a2) - min(x1,a1)
height = max(y2,b2) - min(y1,b1)

x = max(width,height)

print(x*x)