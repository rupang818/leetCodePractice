class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Sounds like recursive...
        # Base-case: if nums[i] == 0, and i < len(nums): return False
        #            if len(nums) <= nums[0]: return True
        # Brute-force: iterate through each nums, and recursively call canJump with nums[i:]
        #               - if false, try jumps of 1 through nums[i] and see if any of them returns T
        # Improvement: memoization -> if the array is known, then return true
        d=set()
        def canJumpMemo(nums):
            if not nums or len(nums) == 1:
                d.add(tuple(nums))
                return True
            elif nums[0] == 0 and 1 < len(nums):
                return False
            elif len(nums) <= nums[0]:
                d.add(tuple(nums))
                return True
            
            if tuple(nums) in d:
                print(d)
                return True
            
            max_reach=nums[0]
            for i in range(1, len(nums)):
                if max_reach < i:
                    return False
                else:
                    max_reach = max(max_reach,nums[i]+i)
            return True
        
        return canJumpMemo(nums)
