# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        m = {}
        def T(r):
            if r is None:
                return
            if r.val in m:
                m[r.val] += 1
            else:
                m[r.val] = 1
            T(r.left)
            T(r.right)
            
        T(root)
        
        r = max(m.values())
        res = []
        for i,v in m.items():
            if v == r:
                res.append(i)
                
        return res