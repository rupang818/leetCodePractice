class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Brute force: a= iterate through the array and set b/c to a permutation and add to the list, if adds up to 0
        # - BUD(Bottleneck/Unnecessary/Duplicate): Once a solution is found with b/c permutation, no need to set pivot at b
        #                                          because w/ a/b combo, there's only 1 possible c to make it 0
        # - To avoid duplicates, keep the solution in a set & make sure each lists are sorted
        # Time: O(n^2)
        
        nums.sort()
        sum3set=set()
        n=len(nums)
        for i in range(n-2):    #Subtract 2 for b/c
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l,r=i+1,n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l+=1
                elif s > 0:
                    r-=1
                else:
                    sum3set.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l+=1
                    r-=1
            
        return [list(i) for i in sum3set]
