# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bst(root):
            if root is None:
                return 0
            lhei = bst(root.left)
            if lhei == -1: return -1
            rhei = bst(root.right)
            if rhei == -1: return -1
            return max(lhei, rhei) + 1 if abs(lhei - rhei) <= 1 else -1

        return bst(root) != -1
