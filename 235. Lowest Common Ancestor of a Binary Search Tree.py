# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minm = min(p.val, q.val)
        maxm = max(p.val, q.val)

        while root:

            if minm <= root.val <= maxm:
                return root

            elif root.val > maxm:
                root = root.left
            else:
                root = root.right
