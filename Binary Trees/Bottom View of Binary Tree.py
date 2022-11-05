def bottomView(self, root):
       # code here
       if root is None:
           return []
          
       m = {}
      
       q = [(0, root)]
       nq = []
       while q:
           for roots in q:
               x, node = roots
               if x in m:
                   m[x] = node.data
               else:
                   m[x] = node.data
          
               if node.left:
                   nq.append((x-1, node.left))
               if node.right:
                   nq.append((x+1, node.right))
           q = nq
           nq = []
      
       res = []
       for i in sorted(m.keys()):
           res.append(m[i])
       return res