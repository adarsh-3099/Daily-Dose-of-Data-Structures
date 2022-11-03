"""Take an empty dictionary and append values at each level (i.e level x)."""

class Solution:
   def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
      
       def vert(r,x,y,values):
           if r is None:
               return
           elif x in values:
               values[x].append((y,r.val))
           else:
               values[x] = [(y,r.val)]
          
           vert(r.left,x-1,y+1,values)
           vert(r.right,x+1,y+1,values)
          
       values = {}
       x = 0
       y = 0
       vert(root,x,y,values)
       print(values)
       res = []
       for i in sorted(values.keys()):
           x = []
           for val in sorted(values[i]):
               x.append(val[1])
           res.append(x)
          
       return res
