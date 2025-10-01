class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1
        numbers = sorted(nums)
        result = 0

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum > k:
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                result += 1
                left += 1
                right -= 1
        return(result)
