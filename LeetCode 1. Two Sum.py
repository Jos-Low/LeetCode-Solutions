nums = [3,3]
target = 6
# Sample TestCase


# Solution in O(n) time
output = []
map = {}
for i, n in enumerate(nums):
    if target - n in map:
        output.append(map[target-n][0])
        output.append(i)
        return output
    if n in map:
        map[n].append(i)
    else:
        map[n] = [i] 


# naive solution
'''
for i, n in enumerate(nums):
    s = target-n
    if s in nums[i+1:]:
        # Test Print
        print([i, nums[i+1:].index(s)+i+1])
'''
