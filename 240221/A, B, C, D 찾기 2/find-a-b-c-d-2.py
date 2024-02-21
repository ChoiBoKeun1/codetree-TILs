arr = list(map(int,input().split()))

ans = []

def func2(tmp_arr, i):
    if i in tmp_arr:
        tmp_arr.remove(i)
    return tmp_arr

def func(arr):
    for a in range(1,40+1):
        for b in range(1,40+1):
            for c in range(1,40+1):
                for d in range(1,40+1):
                    tmp_arr = arr[:]
                    tmp_arr = func2(tmp_arr,d)
                    tmp_arr = func2(tmp_arr,c)
                    tmp_arr = func2(tmp_arr,b)
                    tmp_arr = func2(tmp_arr,a)
                    tmp_arr = func2(tmp_arr,a+b)
                    tmp_arr = func2(tmp_arr,b+c)
                    tmp_arr = func2(tmp_arr,c+d)
                    tmp_arr = func2(tmp_arr,d+a)
                    tmp_arr = func2(tmp_arr,a+c)
                    tmp_arr = func2(tmp_arr,b+d)
                    tmp_arr = func2(tmp_arr,a+b+c)
                    tmp_arr = func2(tmp_arr,a+b+d)
                    tmp_arr = func2(tmp_arr,a+c+d)
                    tmp_arr = func2(tmp_arr,b+c+d)
                    tmp_arr = func2(tmp_arr,a+b+c+d)

                    if len(tmp_arr) == 0:
                        ans.append(a)
                        ans.append(b)
                        ans.append(c)
                        ans.append(d)
                        return

func(arr)
for elem in ans:
    print(elem,end=' ')