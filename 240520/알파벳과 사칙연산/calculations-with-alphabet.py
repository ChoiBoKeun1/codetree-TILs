s = input()

n = len(s)

nums = []
cmds = []

for elem in s:
    if elem == '+' or elem == '-' or elem == '*':
        cmds.append(elem)

num_nums = n // 2 +1
num_cmds = n // 2

ans = 0

def recursive(cnt):
    global ans

    if cnt == num_nums:
        ans = max(ans, calculate())
        return

    for i in range(1,5):
        nums.append(i)
        recursive(cnt +1)
        nums.pop()


def calculate():
    result = 0
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