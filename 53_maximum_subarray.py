import sys

#fix for tle need O(n) solution for timing

nums = [-2, -3, 4, -1, -2, 1, 5, -3]

max_overall = -9999999999
max_cur = 0

for i in range(len(nums)):
    max_cur = max_cur + nums[i]
    if max_overall < max_cur:
        max_overall = max_cur
    if max_cur < 0:
        max_cur = 0
print(max_overall)