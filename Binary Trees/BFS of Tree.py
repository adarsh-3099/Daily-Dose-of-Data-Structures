class Solution:
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      
       if not root:
           return []
      
       q = [root]
       nq = []
       l = []
       res = []
      
       while q:
           for r in q:
               l.append(r.val)
               if r.left:
                   nq.append(r.left)
               if r.right:
                   nq.append(r.right)
           res.append(l)
           l = []
           q = nq
           nq = []
          
       return res
