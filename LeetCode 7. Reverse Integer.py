x = -123
# Example Test Case

if int(str(int(abs(x)))[::-1]) >= 2**31:
    print(0) # Printing to test

if x < 0:
    print(int("-" + str(abs(x))[::-1])) # Printing to test

else:
    print(int(str(x)[::-1])) # Printing to test
