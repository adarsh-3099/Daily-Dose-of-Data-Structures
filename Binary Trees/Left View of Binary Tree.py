def LeftView(root):
   if not root:
       return []
  
   res = []
   q = [root]
   nq = []
   l = []
   while q:
       for r in q:
           l.append(r.data)
           if r.left:
               nq.append(r.left)
           if r.right:
               nq.append(r.right)
              
       res.append(l[0])
       l = []
       q = nq
       nq= []      
   return res
