x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

# 안겹치는 경우
if x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1:
    print("nonoverlapping")
else:
    print("overlapping")

'''
x1,y2   x2,y2   a1,b2   a2,b2

x1,y1   x2,y1   a1,b1   a2,b1
'''