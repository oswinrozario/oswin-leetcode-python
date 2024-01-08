# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if(root is None):
            return 0
        answer = 0
        if(root.val >= low and root.val <= high):
            answer +=  root.val
        return answer + self.range_sum_bst(root.left, low, high) + self.range_sum_bst(root.right, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.range_sum_bst(root,low,high)
        