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


def test_balanced_tree(sol: Solution):
    tree1 = TreeNode(3)
    tree1.left = TreeNode(9)
    tree1.right = TreeNode(20)
    tree1.right.left = TreeNode(15)
    tree1.right.right = TreeNode(7)
    assert sol.isBalanced(tree1)


def test_unbalanced_tree(sol: Solution):
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(2)
    tree2.left.left = TreeNode(3)
    tree2.left.right = TreeNode(3)
    tree2.left.left.left = TreeNode(4)
    tree2.left.left.right = TreeNode(4)

    assert not sol.isBalanced(tree2)


if __name__ == '__main__':
    s = Solution()
    test_balanced_tree(s)
    test_unbalanced_tree(s)
