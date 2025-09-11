s = "dvdfsccsdvgbgdhfyfhfynfn"
# Example TestCase
res = [""] 
current_sub = "" 

for char in s:
    if char in current_sub:
        
        if len(current_sub) > len(res[0]):
            res[0] = current_sub

        current_sub = current_sub[current_sub.index(char)+1:] + char
    else:
        current_sub += char

# Final check in case the longest substring is at the end
if len(current_sub) > len(res[0]):
    res[0] = current_sub

# Print to test 
print(res[0])
