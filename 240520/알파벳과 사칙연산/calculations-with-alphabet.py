s = input()

n = len(s)

# num_mapper[0] = 1 --> a 에 1을 대입시키겠다는 뜻
# num_mapper[3] = 2 --> c에 3를 대입시키겠다는 뜻
num_mapper = []
nums = []
cmds = []

for elem in s:
    if elem == '+' or elem == '-' or elem == '*':
        cmds.append(elem)

num_nums = n // 2 +1
num_cmds = n // 2

ans = 0

def recursive(cnt):
    global ans, num_mapper

    if cnt == num_nums:
        make_nums()
        ans = max(ans, calculate())
        return

    for i in range(1,5):
        num_mapper.append(i)
        recursive(cnt +1)
        num_mapper.pop()

def make_nums():
    global nums

    nums = []
    for elem in s:
        if 'a' <= elem and elem <= 'f':    
            nums.append(num_mapper[ord(elem) - ord('a')])

def calculate():
    result = 0
    
    # 식이 문자 하나만 있는 경우. ex) a
    if num_cmds == 0:
        return 4

    for i in range(num_cmds):
        if i == 0:
            result += nums[i]    
    
        if cmds[i] == '+':
            result += nums[i+1]
        elif cmds[i] == '-':
            result -= nums[i+1]
        elif cmds[i] == '*':
            result *= nums[i+1]

    return result

recursive(0)
print(ans)