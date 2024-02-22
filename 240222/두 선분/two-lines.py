x1,x2,x3,x4 = map(int,input().split())

if x1 <= x3 and x2 >= x3:
    print("intersecting")
else:
    print("nonintersecting")