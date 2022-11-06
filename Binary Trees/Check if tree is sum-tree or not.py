'''  
→ Traverse tree in postorder and check if the sum of left and right part is equal to root value.
 If yes return 2*root.data as we need to return their sum along with the sum of trees from the tree beneath.
'''

import sys
 
class Solution:
   def isSumTree(self,root):
       # Code here
       def dfs(root):
           if not root:
               return 0
              
           if root.left is None and root.right is None:
               return root.data
              
           left = dfs(root.left)
           right = dfs(root.right)
          
           if left != -sys.maxsize and right != -sys.maxsize and left+right == root.data:
               return 2*root.data
          
           return -sys.maxsize
          
       r = dfs(root)
       if r == -sys.maxsize:
           return 0
       return 1