"""Recursive"""
class Solution:
   def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      
       def T(r):
           if not r:
               return
           self.li.append(r.val)
           T(r.left)
           T(r.right)
          
       self.li = []
       T(root)
       return self.li
	
"""
Iterative
→ Take a stack and store node of tree.
→ Pop the top element and print it then store right child and left child.
"""
class Solution:
   def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      
       def T(r):
           if not r:
               return
           self.li.append(r.val)
           T(r.left)
           T(r.right)
          
       self.li = []
       T(root)
       return self.li
