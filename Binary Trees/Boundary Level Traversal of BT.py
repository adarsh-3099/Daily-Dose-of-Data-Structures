"""
→ Append the root data to the result.
→ Traverse the left side of the tree and append to the result.
→ Traverse the bottom of them tree which are leaves nodes and append the to the result.
→ Traverse right side of the tree but append data in reverse order.
"""

class Solution:
   def printBoundaryView(self, root):
       # Code here
       if not root:
           return
      
       if not root.left and not root.right:
           return [root.data]
      
       res = [root.data]
      
       left = []
       def Left(r):
           if r is None:
               return
           if r.left is None and r.right is None:
               return
           left.append(r.data)
           if r.left is None:
               Left(r.right)
           else:
               Left(r.left)
       Left(root.left)
          
       right = []
       def Right(r):
           if r is None:
               return
           if r.left is None and r.right is None:
               return
           right.append(r.data)
           if r.right is None:
               Right(r.left)
           else:
               Right(r.right)
       Right(root.right)
      
       leaf = []
       def Leaf(r):
           if r is None:
               return
           if r.left is None and r.right is None:
               leaf.append(r.data)
           Leaf(r.left)
           Leaf(r.right)
       Leaf(root)
 
       res.extend(left)
       res.extend(leaf)
       res.extend(right[::-1])
       return res
