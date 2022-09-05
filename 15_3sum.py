import sys

nums = [-1,0,1,2,-1,-4]
nums.sort()
num_dict = {}
out_put = set()

for i in range(len(nums)):
    num_dict[nums[i]] = i

for target in range(len(nums)):
    if target != 0 and nums[target] == nums[target -1]:
        continue
    total = -nums[target]

    for i in range(target + 1, len(nums)):
        complement = total - nums[i]
        if complement in num_dict and num_dict[complement] > i:
            out_put.add((nums[i], complement, -total))
print(out_put)