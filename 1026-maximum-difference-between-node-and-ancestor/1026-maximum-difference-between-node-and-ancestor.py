# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack = [(root, root.val, root.val)]
        max_diff = 0

        while stack:
            node, min_val, max_val = stack.pop()

            if node:
                # Update min and max values encountered so far
                min_val = min(min_val, node.val)
                max_val = max(max_val, node.val)

                # Update the maximum difference if needed
                max_diff = max(max_diff, max_val - min_val)

                # Add left and right children to the stack
                stack.append((node.left, min_val, max_val))
                stack.append((node.right, min_val, max_val))

        return max_diff
