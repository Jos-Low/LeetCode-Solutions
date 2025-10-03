class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        pq = []
        for num in nums:
            heapq.heappush(pq, (-num, num))
        while k > 0:
            max_element = heapq.heappop(pq)[1]
            score += max_element
            updated_value = max_element // 3 + (max_element % 3 != 0)
            heapq.heappush(pq, (-updated_value, updated_value))
            k -= 1
        return score
