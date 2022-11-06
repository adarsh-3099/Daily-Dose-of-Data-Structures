def height(r):
   if r is None:
       return
   return 1 + max(height(r.left), height(r.right))
