class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for f in range(n):
            if n % (f+1) == 0:
                factors.append(f+1)
        try:
            return(factors[k-1])
        except:
            return -1
