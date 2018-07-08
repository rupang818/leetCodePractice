class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if nums[0] == target, return 0
        # if nums[0] > target, search in order (keep incrementing index until nums[n] < target)
        # if nums[0] < target, search from the back (nums[-1]) -> (keep decrementing index until nums[n] > target)
        i=0
        if len(nums) < 1:
            return -1
        elif nums[0] is target:
            return i
        elif nums[i] < target:
            while i < len(nums) and nums[i] <= target:
                if nums[i] == target:
                    return i
                i+=1
        else:
            i=len(nums)-1
            while nums[i] >= target and i >= 0:
                if nums[i] == target:
                    return i
                i-=1
        return -1
