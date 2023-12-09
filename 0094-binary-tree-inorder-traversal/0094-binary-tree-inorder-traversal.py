# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
    
        s = []

        if root.left:
            s = self.inorderTraversal(root.left)

        s.append(root.val)

        if root.right:
            s += self.inorderTraversal(root.right)

        return s
