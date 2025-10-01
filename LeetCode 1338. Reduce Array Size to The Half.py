class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        import heapq 

        freq = {}
        heap = []
        half = len(arr) // 2

        for n in arr:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        for n, count in freq.items():
            heapq.heappush(heap, -count)

        output = 0
        removed = 0

        while removed < half:
            count = heapq.heappop(heap)
            removed -= count
            output += 1

        return output
