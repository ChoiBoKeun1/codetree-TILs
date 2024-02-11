import sys

arr = list(map(int,input().split()))

ans = sys.maxsize

for i in range(6):
    for j in range(i+1,6):
        for k in range(6):
            if k == i or k == j:
                continue
            for l in range(k+1,6):
                if l == i or l == j:
                    continue

                set1,set2,set3 = [],[],arr[:]

                set1.append(arr[i])
                set1.append(arr[j])
                set2.append(arr[k])
                set2.append(arr[l])
                set3[i],set3[j],set3[k],set3[l] = 0,0,0,0
                
                sum_list = [sum(set1),sum(set2),sum(set3)]
                sum_list.sort()

                diff = abs(sum_list[0]-sum_list[2])

                ans = min(ans, diff)

print(ans)