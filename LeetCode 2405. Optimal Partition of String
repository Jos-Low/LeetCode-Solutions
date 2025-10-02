class Solution:
    def partitionString(self, s: str) -> int:
        sub = []
        strng = ""
        for i in s:
            if i not in strng:
                strng += i
            else:
                sub.append(strng)
                strng = i
        sub.append(strng)
        return(len(sub))
