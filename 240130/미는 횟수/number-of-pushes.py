A = input()
B = input()

cnt = 0

while A != B:
    cnt += 1
    A = A[len(A)-1] + A[:len(A)-1]

print(cnt)