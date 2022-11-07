import sys

nums = [0,1]
num = len(nums)
max_reach = 0

for i in range(num):
    if i <= max_reach:
        max_reach = max(i + nums[i], max_reach)
    else:
        break


if max_reach >= len(nums) - 1:
    print('true')
else:
    print('false')


