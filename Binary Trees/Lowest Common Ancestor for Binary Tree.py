class Solution:
   def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      
       res = [p.val, q.val]
       def dfs(r):
           if r is None:
               return
           if r.val in res:
               return r
           left = dfs(r.left)
           right = dfs(r.right)
          
           if left and right:
               return r
           else:
               return left or right
       return dfs(root)
