import heapq
s = "tree"
# Example TestCase

output = ""
heap = []
freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char, count in freq.items():
    heapq.heappush(heap, (-count, char))

while heap:
    count, char = heapq.heappop(heap)
    output += char * (-count)

print(output) # Print to test
