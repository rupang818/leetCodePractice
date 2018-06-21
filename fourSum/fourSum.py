class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1. sort the array (i.e. [-2, -1, 0, 0, 1, 2]) - O(nlogn)
        # 2. if the sumSoFar > target and next elem >= 0: break
        # 3. elif sumSoFar < target and last elem <= 0: break
        nums.sort()
        solution = []
        for i in range(len(nums)-3):
            if nums[i] == nums[i - 1] and i>0:
                continue
            for j in range(i+1,len(nums)-2):
                if nums[j]==nums[j-1] and j>i+1:
                    continue
                l,r = j+1,len(nums)-1
                while l<r:
                    sum = nums[i]+nums[j]+nums[l]+nums[r]
                    if sum ==target:
                        solution.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:l+=1
                        while l<r and nums[r]==nums[r-1]:r-=1
                        l+=1
                        r-=1
                    elif sum>target:
                        r-=1
                    else: l+=1
        return solution
