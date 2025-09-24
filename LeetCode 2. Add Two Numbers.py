l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
# Example TestCase

length1 = len(l1)
length2 = len(l2)
if length1 > length2:
    dif = length1-length2
    l2.extend([0]*dif)
elif length2 > length1:
    dif = length2-length1
    l1.extend([0]*dif)
n1 = ""
n2 = ""
for n in l1[::-1]:
    n1 += str(n)
for n in l2[::-1]:
    n2 += str(n)
total = int(n1) + int(n2)
output = [int(n) for n in str(total)][::-1]

# Print for testing 
print(output)
