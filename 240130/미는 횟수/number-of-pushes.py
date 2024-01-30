A = input()
B = input()

cnt = 0

while A != B:
    cnt += 1
    A = A[len(A)-1] + A[:len(A)-1]
    if cnt == len(A):
        cnt = -1
        break

print(cnt)