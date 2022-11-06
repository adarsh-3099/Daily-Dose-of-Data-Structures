''' 
→ Check if the left tree is equal to right tree as it is required for the tree to be symmetric.
'''

class Solution:
   def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      
       def dfs(r1, r2):
           if not r1 and not r2:
               return
           elif r1 and not r2:
               self.ans = False
               return
           elif not r1 and r2:
               self.ans = False
               return
           elif r1.val != r2.val:
               self.ans = False
               return
           dfs(r1.left, r2.right)
           dfs(r1.right, r2.left)
 
       self.ans = True
       dfs(root, root)
       return self.ans
