class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sort the array in reverse and get the kth element
        nums.sort(reverse=True)
        return nums[k-1]
