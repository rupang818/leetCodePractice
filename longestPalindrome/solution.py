class Solution:    
    palindrome = set()
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if self.isPalindrome(s):
            return s
        else:
            if s[0] is s[-1] and self.isPalindrome(s[1:-1]):
            # print("Symmetric: %s is already known to be palindrome" % s)
                self.palindrome.add(s)
                return s
            else:
                return self.getMaxPalinOfLeftRight(s)
    
    def isPalindrome(self, s):
        if len(s) <= 1:
            # self.palindrome.add(s)
            return True
        elif len(s) == 2:
            retVal = True if (s[0] == s[1]) else False
            if retVal:
                self.palindrome.add(retVal)
            return retVal
        elif s in self.palindrome:
            return True
        else:
            return False
    
    # Take the left & right and return the max lengthed palindrome of the two
    def getMaxPalinOfLeftRight(self, s):
        # Memoization: check if left or right is already a known palindrome
        if self.isPalindrome(s[:-1]):
            # print("L: %s is already known to be palindrome" % s[:-1])
            left = s[:-1]
        else:
            left = self.longestPalindrome(s[:-1])
            if left is not None:
                self.palindrome.add(left)   # memoization
                # print("L: %s is new!" % left)
        
        if self.isPalindrome(s[1:]):
            # print("R: %s is already known to be palindrome" % s[1:])
            right = s[1:]
        else:
            right = self.longestPalindrome(s[1:])
            if right is None:
                return left
            elif left is None:
                self.palindrome.add(right)  # memoization
                return right
            # print("R: %s is new!" % right)
        
        # print("Left: %s, Right: %s" %(left, right) )
        result = left if (len(left) >= len(right)) else right
        # print("Result is: %s" % result)
        return result
        
    def runTest(self, s):
        test = self.longestPalindrome(s)
        print("TEST RESULT: %s" %test)
        return test
    
# sol = Solution()
# sol.runTest("babaddtattarrattatddetar")
# sol.runTest("babaddtattarrattatddetartrateedredividerb")
# sol.runTest("dababadab")