class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        chars = {}
        output = 0
        lowers = []
        for n in range(len(word)):
          if word[n] in chars:
            continue
          if word[n].isupper():
            chars[word[n]] = n
        for n in range(len(word)-1,-1,-1):
          w = word[n]
          count = 0
          if word[n].islower():
            if w.upper() in chars:
              if w in lowers:
                continue
              if chars[w.upper()] < n:
                del chars[w.upper()]
              elif chars[w.upper()] > n:
                  count = 1   
                  lowers.append(w)    
          output += count
        return output
