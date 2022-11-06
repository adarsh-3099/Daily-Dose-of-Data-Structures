class Solution:
   def isValidBST(self, root: Optional[TreeNode]) -> bool:
       def validate(root, l1, r1):
           if root is None:
               return True
           if root.val <= l1 or root.val >= r1:
               return False
           l = validate(root.left, l1, root.val)
           r = validate(root.right, root.val, r1)
           return l and r
       return validate(root, -1*2**31-1, 2**31-1+1)
