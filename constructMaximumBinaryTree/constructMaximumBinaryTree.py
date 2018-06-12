class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # identify max index, make it a root, pass left arr recursively & pass right arr recursively
        # max=6, left=constructMaximumBinaryTree([3,2,1]).root, right=constructMaximumBinaryTree([0,5]).root
        # left=> max=3, left=None, right=[2,1] => max=2, left=None, right=[1]
        # right=> max=5, left=[0], right=None
        #
        # Base-case: len(nums) == 1, return TreeNode(nums[0])
        #            nums empty, return None
        if not nums:
            return None
        elif len(nums) is 1:
            return TreeNode(nums[0])
        else:
            left=[]
            right=[]
            maxSoFar=nums[0]
            for i in range(1,len(nums)):
                if nums[i] > maxSoFar:
                    left.append(maxSoFar)
                    maxSoFar=nums[i]
                    left+=right
                    right=[]
                else:
                    right.append(nums[i])
            root=TreeNode(maxSoFar)
            root.left=self.constructMaximumBinaryTree(left)
            root.right=self.constructMaximumBinaryTree(right)

            return root
