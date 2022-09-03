import sys

height = [1,8,6,2,5,4,8,3,7]

area = 0
left = 0
right = len(height) - 1

while left < right:
    area = max(min(height[left], height[right]) * abs(right - left), area)
    if height[left] <= height[right]:
        left += 1
    elif height[left] > height[right]:
        right -= 1
print(area)