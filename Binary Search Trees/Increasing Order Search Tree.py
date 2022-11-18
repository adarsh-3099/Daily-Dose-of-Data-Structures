# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        li = []
        def T(r):
            if r is None:
                return
            T(r.left)
            li.append(r.val)
            T(r.right)
            
        def cre(li):
            if not li:
                return 
            root = TreeNode(li[0])
            root.right = cre(li[1:])
            return root
        
        T(root)
        r = cre(li)
        return r