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
        left_level = 0
        if root.left != None:
            left_level = maxDepth(root.left)
        right_level = 0
        if root.right != None:
            right_level = maxDepth(root.right)
        return max(left_level, right_level) + 1
