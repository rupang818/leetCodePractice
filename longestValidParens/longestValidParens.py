class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """        
        validParens = [-1]
        maxLen = 0
        for i in range(len(s)):
            if s[i] is "(":
                validParens.append(i)   # [0, 3]
            else:
                validParens.pop()        # []
                if len(validParens) is 0:
                    validParens.append(i)   # [5]
                maxLen = max(i - validParens[-1], maxLen)    # 4-0=4
        return maxLen
