'''  
→ The diameter is just the longest path between any two nodes.
→ So at every node we will find height to it’s left tree and height of it’s right side of tree.
→ If sum of leftTree + rightTree is more then current diameter simply update the result.
'''

class Solution:
   def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      
       def hei(r):
           if r is None:
               return 0
           return 1+max(hei(r.left),hei(r.right))
      
       def dfs(r):
           if r is None:
               return 0
           lh = hei(r.left)
           rh = hei(r.right)
           self.res = max(self.res, rh+lh)
           dfs(r.left)
           dfs(r.right)
      
       self.res = 0
       dfs(root)
       return self.res
