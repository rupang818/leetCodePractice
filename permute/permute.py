class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Brute force: for each elements, iterate through each of the following elements. O(n!)
        if len(nums)<=1:
            return [nums]
        else:
            i=0
            output=[]
            while i < len(nums):
                newlist=nums[:i] + nums[i+1:]
                for x in self.permute(newlist):
                    x.insert(0,nums[i])
                    output.append(x)
                i+=1
            return output
