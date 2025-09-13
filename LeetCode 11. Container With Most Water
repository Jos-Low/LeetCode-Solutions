height = [1,8,6,2,5,4,8,3,7]
# Testcase
most = 0
left = 0
right = len(height) - 1

while left < right:
    area = min(height[left], height[right]) * (right - left)
    most = max(most, area)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
# Print to test
print(most)
