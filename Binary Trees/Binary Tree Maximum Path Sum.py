class Solution:
   def maxPathSum(self, root: TreeNode) -> int:
       ans = root.val
       def dfs(root):
           nonlocal ans
           if root is None:
               return 0
           left = dfs(root.left)
           right = dfs(root.right)
           ans = max(root.val+left+right,ans)
           ans = max(root.val+left,ans)
           ans = max(root.val+right,ans)
           ans = max(root.val,ans)
           return max(root.val,root.val+left,root.val+right)
      
       dfs(root)
       return ans
