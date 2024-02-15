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
    cnt = 1
    for j in range(n):
        if i == j:
            continue

        j_price = arr[j].get_full_price()
        total_price += j_price
        
        if b < total_price:
            total_price -= j_price
        else:
            cnt += 1

    ans = max(ans,cnt)

print(ans)