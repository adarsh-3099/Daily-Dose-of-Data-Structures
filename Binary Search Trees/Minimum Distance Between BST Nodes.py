# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        li = []
        if not root:
            return 0
        
        def T(r):
            if r:
                li.append(r.val)
                T(r.left)
                T(r.right)
            
        T(root)
        li.sort()
        print(li)
        
        m = 2**31-1
        i=0
        j=1
        n=len(li)
        while j<n:
            m = min(m,abs(li[j]-li[i]))
            j+=1
            i+=1
        return m