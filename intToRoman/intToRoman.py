class Solution:
    romanDict = {1:"I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        currDenom=10
        currNum=num
        strSoFar=""
        while currNum is not 0:
            strSoFar = self.helper(currNum, currDenom) + strSoFar
            currNum -= currNum % currDenom
            currDenom*=10
        return strSoFar
    
    # TODO: handle muldtiple digits
    # If "I", "X", "C" is found, chcek the immediate next one as well
    # - if next is V/X, L/C, D/M (respectively), then current char is negative
    # - if not, carry on

    def helper(self, num, lowestDenom):
        lastDigit = num % lowestDenom
        halfDenom = round(lowestDenom/2)
        stringSoFar = ""
        if lastDigit in self.romanDict:
            stringSoFar = self.romanDict[lastDigit] + stringSoFar
        else:
            if lastDigit > halfDenom:
                stringSoFar =  self.romanDict[halfDenom] + self.helper(num- halfDenom, lowestDenom) + stringSoFar
            else:
                numberAtTheDigit=round(lastDigit/round(lowestDenom/10))
                for _ in range(numberAtTheDigit):
                    stringSoFar += self.romanDict[lowestDenom/10]
        return stringSoFar
