# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def T(r):
            if r is None:
                return
            T(r.left)
            li.append(r.val)
            T(r.right)
            
        li = []
        T(root)
        #print(li)
        
        def build(arr):
            if not arr:
                return 
            m = len(arr)//2
            root = TreeNode(arr[m])
            root.left = build(arr[:m])
            root.right = build(arr[m+1:])
            return root
        
        r = build(li)
        return r