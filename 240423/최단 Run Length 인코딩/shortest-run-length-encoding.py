a = list(input())

def shift(string):
    length = len(string)

    tmp = string[length-1]

    for i in range(length-1, 0, -1):
        string[i] = string[i-1]
    
    string[0] = tmp

def run_length_encoding(string):
    new_arr = []
    
    length = len(string)
    cnt = 1
    for i in range(length-1):
        if string[i+1] == string[i]:
            cnt += 1
        
        else:
            new_arr.append(string[i])
            new_arr.append(str(cnt))
            cnt = 1

    new_arr.append(string[length-1])
    new_arr.append(str(cnt))

    new_str = ""

    for elem in new_arr:
        new_str += elem
    
    return new_str


length = len(a)

ans = 100

for _ in range(length):
    shift(a)   
    encoded_length = len(run_length_encoding(a))
    ans = min(ans,encoded_length)

print(ans)