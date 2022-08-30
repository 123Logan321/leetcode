import sys

nums = list(sys.stdin.readline().replace(" ", "").strip())
target = int(sys.stdin.readline())

num_dict = {}
for i in range(len(nums)):
    num_dict[int(nums[i])] =  int(i)

for i in range(len(nums)):
    complement = target - int(nums[i])
    if complement in num_dict and num_dict[complement] != i:
        print([i, num_dict[complement]])
    