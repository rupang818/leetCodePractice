# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            leftDepth=0
            rightDepth=0
            if root.left:
                leftDepth=self.maxDepth(root.left)
            if root.right:
                rightDepth=self.maxDepth(root.right)
            return 1 + max(leftDepth,rightDepth)
