class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        arrOfStrings = ["" for x in range(numRows)]
        i = 0
        row = 0
        while i < len(s):
            downUp = math.floor(i/(numRows-1)) % 2
            arrOfStrings[row] += s[i]
            row += 1 if downUp == 0 else -1
            i+=1
            
        returnS = ""
        for s in arrOfStrings:
            returnS+=s
        return returnS
