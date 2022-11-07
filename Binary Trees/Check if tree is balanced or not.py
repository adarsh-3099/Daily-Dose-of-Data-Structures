class Solution:
   def isBalanced(self, root: Optional[TreeNode]) -> bool:
      
       def hei(r):
           if r is None:
               return 0
           return 1 + max(hei(r.left), hei(r.right))
      
       def bal(r):
           if r is None:
               return True
          
           lh = hei(r.left)
           rh = hei(r.right)
          
           if abs(lh-rh) > 1:
               return False
          
           l = bal(r.left)
           r = bal(r.right)
          
           return l and r
      
       ans = bal(root)
       return ans
