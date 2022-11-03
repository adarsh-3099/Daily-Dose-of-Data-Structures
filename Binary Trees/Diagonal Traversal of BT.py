"""  
→ The key is to use dict to store the diagonal elements.
→ It’s similar to vertical order only that diagonal value does not change for right node as right elements are in same diagonal.
"""

class Solution:
   def diagonal(self,root):
       #:param root: root of the given tree.
       #return: print out the diagonal traversal,  no need to print new line
       #code here
       if not root:
           return []
          
       def diagonal(diag, d, r):
           if not r:
               return
           if diag not in d:
               d[diag] = [r.data]
           else:
               d[diag].append(r.data)
          
           diagonal(diag+1, d, r.left)
           diagonal(diag, d, r.right)
          
      
       d = {}
       diagonal(0, d, root)
       res = []
       for i in sorted(d.keys()):
           for val in d[i]:
               res.append(val)
      
       return res
 
