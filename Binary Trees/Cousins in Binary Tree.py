''' 
→ We will take an array of tuples and keep track of level, parent and node value
→ Then we will see if the if the value x and y has same level and different parents or not if yes return True else return False.
'''


class Solution:
   def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
 
       q = [(root, -1)]
       nq = []
       res = []
       i = 0
       while q:
           for r in q:
               node, par = r
               res.append((i, node.val, par))
               if node.left:
                   nq.append((node.left, node.val))
 
               if node.right:
                   nq.append((node.right, node.val))
 
           i += 1
           q = nq
           nq = []
      
       par = []
       for item in res:
           if item[1] == x or item[1] == y:
               par.append((item[0], item[-1]))
      
       print(res)
       print(par)
 
       if len(par) != 2:
           return False
      
       if ((par[0][0] == par[-1][0]) and (par[0][1] != par[-1][1])):
           return True
 
       return False
