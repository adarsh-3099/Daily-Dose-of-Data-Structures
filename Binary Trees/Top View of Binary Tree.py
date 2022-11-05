"""If in Vertical order traversal we keep only the first element for any key it’ll give us Top View of BT."""

# BFS Solution

def topView(self,root): 
       if root is None:
           return []
          
       m = {}
       q = [(0, root)]
       nq = []
      
       while q:
           for r in q:
               i, node = r
               if i not in m:
                   m[i] = node.data
              
               if node.left:
                   nq.append((i-1, node.left))
              
               if node.right:
                   nq.append((i+1, node.right))
           q = nq
           nq = []
      
       res = []
       print(m)
       for i in sorted(m.keys()):
           res.append(m[i])
       return res


# DFS Solution

def topView(self,root):
       if not root:
           return
 
       def vert(x, y, r, d):
           if r is None:
               return
           if x not in d:
               d[x] = r.data
           vert(x-1, r.left, d)
           vert(x+1, r.right, d)
      
       d = {}
       x = 0
       vert(x, root, d)
       res = []
       for i in sorted(d.keys()):
           res.append(d[i])
       return res

