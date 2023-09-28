# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root, left, right):
            if not root:
                return True
            if not (right > root.val and left < root.val):
                return False

            l = solve(root.left, left, root.val)
            r = solve(root.right, root.val, right)
            if l and r:
                return True

        return solve(root, float("-inf"), float("inf"))
