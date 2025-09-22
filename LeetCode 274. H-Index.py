citations = [3,0,6,1,5]
# Example Testcase

citations.sort()
h = 0
for i, num in enumerate(citations[::-1]):
    if num >= i + 1:
        h = i + 1
    else:
        break
print(h)   # Print for testing
