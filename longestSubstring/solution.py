class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window: keep a set of CharSoFar (chars collected so far) and return the maxSofar: 
        #               - Time: O(2n), since a same index can be visited multiple times 
        #               - Space: O(min(m,n)), since the set will contain only the subset of m or n (all unique characters)
        i=0
        j=0
        maxSoFar=""
        charSet=set()
        while i < len(s) and j <= len(s):
            # print("i:%s, j:%s, s[i:j]:%s" %(i,j,s[i:j]))
            if j == len(s):
                if len(maxSoFar) < len(s[i:j]):
                    maxSoFar=s[i:j]
                break
            elif s[j] in charSet:
                if len(maxSoFar) < len(s[i:j]):
                    maxSoFar=s[i:j]
                i+=1
                j=i
                charSet=set()
            else:
                charSet.add(s[j])
                j+=1
        return len(s) if len(maxSoFar)==0 else len(maxSoFar)
