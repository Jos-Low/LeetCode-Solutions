class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        pilegroups = len(piles) // 3
        AliceYou = []
        You = 0
        for n in range(len(piles)):
          if n < pilegroups:
            continue
          else:
            AliceYou.append(piles[n])
        for x in range(len(AliceYou)):
          if x % 2 == 0:
            You += AliceYou[x] 
        return You
