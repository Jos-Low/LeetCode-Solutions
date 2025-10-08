s = "()))(())())((()()()))"
locked = "010000100000000000000"
# Test Case

valpar = []
valid = 0
if len(s) % 2 != 0:
    valid = valid + 1
for n in range(len(s)):
    char = s[n]
    prevchar = s[n-1]
    if n == len(s)-1:
        if prevchar == char:
            valpar.append(1)
        else:
            valpar.append(0)
        break
    nextchar = s[n+1]
    if char == ")":
        if nextchar == ")" and prevchar == ")":
            valpar.append(1)
        else:
            valpar.append(0)
    elif char == "(":
        if nextchar == "(" and prevchar == "(":
            valpar.append(1)
        else:
            valpar.append(0)
for x in range(len(valpar)):
    if valpar[x] == 1 and int(locked[x]) == 1:
      valid = valid + 1
    else:
      continue
if valid > 0:
    print(False)
else:               # Print to test
    print(True)
