# Recursive
class Solution:
   def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       if not root:
           return []
      
       res = []
       st = [root]
       while st:
           node = st.pop()
           res.append(node.val)
           if node.left:
               st.append(node.left)
           if node.right:
               st.append(node.right)
              
       return res[::-1]

# Iterative
class Solution:
   def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       if not root:
           return []
      
       res = []
       st = [root]
       while st:
           node = st.pop()
           res.append(node.val)
           if node.left:
               st.append(node.left)
           if node.right:
               st.append(node.right)
              
       return res[::-1]
