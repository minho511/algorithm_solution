import sys; input = sys.stdin.readline

def round_(num):
    if num - int(num) >= 0.5: return int(num+1)
    return int(num)

n = int(input())
if n == 0:
    print(0)
    exit()

nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()
a = round_(n*0.15)
if a > 0:
    nums = nums[a:-a]
sum_ = sum(nums)
print(round_(sum(nums)/len(nums)))