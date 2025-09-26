num = [1,2,0,5,0]
k = 34
# TestCase

number = 0
output = []
for n in num:
    number = number *10 + n
number = number + k
for x in str(number):
    output.append(int(x))

#Print to test
print(output)    
