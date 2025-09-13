num = 3749
numerals = [(1000, 'M'),(900, 'CM'),(500, 'D'),(400, 'CD'),(100, 'C'),(90, 'XC'),
               (50, 'L'),(40, 'XL'),(10, 'X'),(9, 'IX'),(5, 'V'),(4, 'IV'),(1, 'I')]
# TestCASE

output = []
for number in numerals:
    while num >= number[0]:
        num -= number[0]
        output += number[1]

# Test print
print("".join(output))
