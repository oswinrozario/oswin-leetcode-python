# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaf(self, root: Optional[TreeNode], leaf: List[int]):
        if root is None:
            return
        if(root.left is None and root.right is None):
            leaf.append(root.val)
            return
        self.getLeaf(root.left,leaf)
        self.getLeaf(root.right,leaf)

        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leaf1 = []
        self.getLeaf(root1,leaf1)
        leaf2 = []
        self.getLeaf(root2,leaf2)

        return leaf1 == leaf2

        