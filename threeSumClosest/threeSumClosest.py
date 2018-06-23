class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # keep a running "sumSoFar" and if a new solution is found that yields less, then set it
        # sorting (O(nlogn)) benefit? possibly
        # for every i, explore j/k that will yield closest target.
        # if on target, return the numbers
        sortedNums = sorted(nums) # [-4,-1,1,2]
        
        if len(sortedNums) < 3:
            return 0
        
        closestSumSoFar = sortedNums[0] + sortedNums[1] + sortedNums[2]
        for i in range(len(sortedNums) -2):
            left,right=i+1,len(sortedNums)-1
            while left < right:
                currSum = sortedNums[i] + sortedNums[left] + sortedNums[right]
                
                if abs(currSum-target) < abs(closestSumSoFar-target):
                    closestSumSoFar = currSum
                
                if currSum < target:
                    left+=1
                else:
                    right-=1
        return closestSumSoFar
        
