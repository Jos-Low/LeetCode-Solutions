s = "acsdvjbhracecarhjjsvskbvs"
# Test Case
palindrome = [""]
count = 0
# if len(s) == 1:
#     print(s)
while count < len(s):
    start = 0
    end = len(s) - count
    for i in range(count+1):
        chunk = s[start:end]
        if chunk == chunk[::-1] and len(chunk) > len(palindrome[0]):
            palindrome[0] = chunk
        # print(s[start:end])
        start += 1
        end += 1
    count += 1
# Print for testing
print(palindrome[0])
