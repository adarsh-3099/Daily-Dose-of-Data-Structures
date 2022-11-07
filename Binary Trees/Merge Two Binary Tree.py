class Solution:
   def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
      
       def T(r1, r2):
           if not r1 and not r2:
               return
           elif not r1:
               return r2
           elif not r2:
               return r1
           else:
               r1.val += r2.val
           r1.left = T(r1.left, r2.left)
           r1.right = T(r1.right, r2.right)
           return r1
 
       r = T(root1, root2)
       return r
