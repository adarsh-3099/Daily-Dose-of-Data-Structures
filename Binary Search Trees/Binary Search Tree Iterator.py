# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        def dfs(r, l):
            if r is None:
                return 
            dfs(r.left, l)
            l.append(r.val)
            dfs(r.right, l)
            return l
            
        self.root = root      
        self.li = dfs(self.root, [])
        self.i = 0
        print(self.li)
        
    def next(self) -> int:
        x = self.li[self.i]
        self.i += 1
        return x

    def hasNext(self) -> bool:
        if self.i == len(self.li):
            return False
        return True
        
