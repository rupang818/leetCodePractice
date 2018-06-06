class Solution:
    romanDict = {"I": 1, "V":5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Recursive look ahead window method:
        # Read from the front, and subtract values encountered from the total then recurse with left over
        # if I,X or C is encountered, read the next letter to make sure the value is less, then jump 1
        #                           , if not, subtract the read char's value from total, then jump 2
        #                           , if equal, add to total, then jump 1
        # else, simply add to the toal, then jump 1
        
        total=0
        if len(s) is 0:
            return 0
        elif len(s) is 1:
            return self.romanDict[s[0]]
        else:
            firstChar=s[0]
            secondChar=s[1]
            if firstChar is "I" or "X" or "C":
                if self.romanDict[firstChar] < self.romanDict[secondChar]:
                    return self.romanToInt(s[1:]) - self.romanDict[firstChar]
                else:
                    return self.romanDict[firstChar] + self.romanToInt(s[1:])
            else:
               return self.romanDict[firstChar] + self.romanToInt(s[1:]) 
