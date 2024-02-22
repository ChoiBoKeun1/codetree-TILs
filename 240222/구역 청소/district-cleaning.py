a,b = map(int,input().split())
c,d = map(int,input().split())

def intersecting(x1,x2,x3,x4):
    if x2 < x3 or x4 < x1:
        return False
    else:
        return True

'''
겹치는 경우
a     c     b      d
c     a     d      b
두 선분의 오른쪽 값들 중 큰 값 - 두 선분의 왼쪽 값들 중 작은 값
'''
if intersecting(a,b,c,d):
    print(max(b,d) - min(a,c))
else:
    print((b-a)+(d-c))