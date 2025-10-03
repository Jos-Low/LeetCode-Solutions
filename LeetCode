class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for r in nums:
            r.sort(reverse=True)

        sum = 0
        i = 0
        while i < len(nums[0]):
            max_n = 0
            for r in nums:
                if r[i] > max_n:
                    max_n = r[i]
            sum += max_n
            i += 1
            
        return sum
