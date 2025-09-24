import heapq
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
# Example test case

heap = []
freq = {}
output = []

for word in words:
    if word in freq:
        freq[word] +=1
    else:
        freq[word] = 1

for word, count in freq.items():
    heapq.heappush(heap, (-count, word))

for n in range(k):
    count, word = heapq.heappop(heap)
    output.append(word)

# Print to test
print(output)
