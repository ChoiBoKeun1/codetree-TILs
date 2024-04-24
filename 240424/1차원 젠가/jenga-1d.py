n = int(input())
tower = [0] + [
    int(input())
    for _ in range(n)
]

def remove(tower, start, end):
    tmp = [0]
    for i in range(1,len(tower)):
        if start <= i and i <= end:
            continue
        
        tmp.append(tower[i])

    return tmp


s1,e1 = map(int,input().split())
tower = remove(tower, s1,e1)

s2,e2 = map(int,input().split())
tower = remove(tower, s2,e2)

print(len(tower)-1)
for i in range(1,len(tower)):
    print(tower[i])