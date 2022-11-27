class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        
        rex = []
        li = []
        def T(r):
            if r is None:
                return 
            T(r.left)
            li.append(r.val)
            rex.append(r)
            T(r.right)
        T(root)
        
        li.sort()
        print(li)
        for i in range(len(rex)):
            rex[i].val = li[i]