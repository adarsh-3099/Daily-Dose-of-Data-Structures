class Solution:
   def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
      
       dp = {}
       def back(n):
           if n == 0:
               return []
 
           if n == 1:
               return [TreeNode()]
 
           if n in dp:
               return dp[n]
 
           res = []
           for l in range(n):
               r = n - 1 - l
               lTree, rTree = back(l), back(r)
 
               for t1 in lTree:
                   for t2 in rTree:
                       res.append(TreeNode(0, t1, t2))
          
           dp[n] = res
           return res
 
       return back(n)
