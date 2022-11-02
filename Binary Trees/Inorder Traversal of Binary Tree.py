"""Recursive"""
class Solution:
   def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      def T(r):
           if not r:
               return
           T(r.left)
           self.li.append(r.val)
           T(r.right)
 
      self.li = []
      T(root)
      return self.li

"""Iterative
	→ Take a stack and append root to it.
→ Run loop till stack is not empty and pop() top element.
→ If node is not empty append left child to stack, print the node and append the right child."""
class Solution:
   def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       ret = []
       stack = [root]
       while stack:
           node = stack.pop()
           if node:
               stack.append(node.left)
               ret.append(node.val)
               stack.append(node.right)
       return ret
