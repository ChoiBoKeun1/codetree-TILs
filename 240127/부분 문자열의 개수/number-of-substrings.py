A = input()
B = input()

cnt = 0

for i in range(len(A)-1):
    if B[0] == A[i] and B[1] == A[i+1]:
        cnt += 1

print(cnt)