# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
from collections import deque


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        xs = []

        q = deque()
        q.append(root)
        while len(q) > 0:
            total = 0.0
            length = len(q)
            for i in range(length):
                root = q.popleft()
                total += root.val
                if root.left != None:
                    q.append(root.left)
                if root.right != None:
                    q.append(root.right)
            xs.append(total / length)
        return xs
