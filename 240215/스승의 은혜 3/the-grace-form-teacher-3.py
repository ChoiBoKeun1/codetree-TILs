class Student:
    def __init__(self, p, s):
        self.p, self.s = p,s

    def get_full_price(self):
        return self.p + self.s
    def get_sale_price(self):
        return self.p // 2 + self.s

n,b = map(int,input().split())

arr = []

for _ in range(n):
    p,s = map(int,input().split())
    arr.append(Student(p,s))

ans = 0
# i번째 학생에게 할인 쿠폰을 적용
for i in range(n):
    total_price = arr[i].get_sale_price()
    
    if b < total_price:
        continue
    
    cnt = 1
    tmpArr = arr[:]
    tmpArr.pop(i)
    sorted_tmpArr = sorted(tmpArr,key=lambda x: x.get_full_price())
    
    for j in range(n-1):
        if i == j:
            continue

        total_price += sorted_tmpArr[j].get_full_price()
        
        if b < total_price:
            break
        else:
            cnt += 1

    ans = max(ans,cnt)

print(ans)