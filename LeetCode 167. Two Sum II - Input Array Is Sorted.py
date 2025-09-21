numbers = [2,7,11,15]
target = 9
# Example TestCase

for n in range(len(numbers)):
            num = numbers[n]
            left = numbers[n+1:]
            if (target - num) in left:
                print([n+1,left.index(target-num)+(n+2)])   # Print to test
