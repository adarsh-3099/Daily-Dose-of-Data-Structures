class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        if n == 0:
            return []
        
        def helper(start, end):
            if start > end:
                return [None]
            
            res = []
            
            for i in range(start, end+1):
                #root = TreeNode(i)
                left = helper(start, i-1)
                right = helper(i+1, end)
                
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        
                        res.append(root)  
            return res
        
        return helper(1, n)