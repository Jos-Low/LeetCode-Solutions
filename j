nums = [9,8,1,0,1,9,4,0,4,1]
# Example TestCase

ramps = []
for n in range(len(nums)):
  widths = [0]
  for x in range(len(nums)):
    width = x-n
    if nums[n] <= nums[x]:
      if width > widths[0]:
        widths.clear()
        widths.append(width)
  ramps.append(widths)    
ramps.sort()

#Print to test
print(ramps[-1][0])
