# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                return None
            if not root.right and root.left:
                return root.left
            if root.right and not root.left:
                return root.right
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)

        return root


if __name__ == '__main__':
    s = Solution()
    tree1 = TreeNode(5)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(6)
    tree1.left.left = TreeNode(2)
    tree1.left.right = TreeNode(4)
    tree1.right.left = TreeNode(None)
    tree1.right.right = TreeNode(7)
    key = 3
    ans = s.deleteNode(tree1, key)
    print(ans)
