class Solution:
   def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      
       if not root:
           return []
      
       q = [root]
       nq = []
       res = []
       l = []
       i = 0
      
       while q:
           for r in q:
               l.append(r.val)
               if r.left:
                   nq.append(r.left)
               if r.right:
                   nq.append(r.right)
           if i % 2 == 0:
               res.append(l)
           else:
               res.append(l[::-1])
           l = []
           q = nq
           nq = []
           i += 1
       return res
