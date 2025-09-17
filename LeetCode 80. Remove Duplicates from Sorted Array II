nums = [0,0,1,1,1,1,2,3,3]
# Example TestCase
number = {}
for i, n in enumerate(nums):
    if n not in number:
        number[n] = 1
    else:
        number[n] += 1

for key in number:
    while number[key] > 2:
        nums.remove(key)
        number[key] -= 1
print(nums) # Print to test
