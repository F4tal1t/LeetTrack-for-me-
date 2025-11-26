# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mini = 10**6
        prev_val = float('-inf')

        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root =  stack.pop()
                mini =  min(mini , root.val -prev_val)
                prev_val = root.val
                root = root.right
        return mini