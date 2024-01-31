Y,M,D = map(int,input().split())

def isLeapYear(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    return False
    
def checkMonth(m):
    _31days = [1,3,5,7,8,10,12]
    _30days = [4,6,9,11]
    
    if m in _31days:
        return 31
    elif m in _30days:
        return 30
    else:
        return 28

# 연월일 존재유무 check
def checkYMD(Y,M,D):
    # 연월일이 존재하지 않으면, -1 print 후 False 리턴.
    max_days = checkMonth(M)

    # 윤년일 경우
    if isLeapYear(Y):
        if max_days == 28:
            max_days += 1
        if D > max_days:
            print("-1")
            return False

    # 윤년이 아닐 경우
    else:
        if D > max_days:
            print("-1")
            return False
    
    # 연월일이 존재하면, True 리턴.
    return True


if checkYMD(Y,M,D):
    if M >= 3 and M <= 5:
        print("Spring")
    elif M >= 6 and M <= 8:
        print("Summer")
    elif M >= 9 and M <= 11:
        print("Fall")
    elif M == 12 or M <= 2:
        print("Winter")