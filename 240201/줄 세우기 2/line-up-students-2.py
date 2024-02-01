class Student:
    def __init__(self, h, w, number):
        self.h, self.w, self.number = h, w, number


N = int(input())

students = []

for i in range(N):
    h,w = map(int,input().split())
    s = Student(h,w, i+1)
    students.append(s)

sorted_s = sorted(students, key=lambda student: (student.h, -student.w))

for s in sorted_s:
    print(s.h, s.w, s.number)