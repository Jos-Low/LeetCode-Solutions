class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ""
        prev = 0
        for sp in spaces:

            output += s[prev:sp] + " "
            prev = sp
        output += s[prev:]
        return(output)
