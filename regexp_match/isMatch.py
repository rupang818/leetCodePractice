class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #Base-case: if there's no pattern given, return not s (for empty p &s, returns true)
        if not p:
            return not s
        
        # First char match
        first_match = bool(s) and p[0] in {".", s[0]}
        
        if len(p) >=2 and p[1] == "*":  # match "*"
            # match greedily
            return (self.isMatch(s,p[2:]) or
                    first_match and self.isMatch(s[1:],p))
        else:
            return first_match and self.isMatch(s[1:],p[1:])
