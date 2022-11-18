class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search(root, val):
            if root is None:
                return 
            if root.val == val:
                return root
            l = search(root.left, val)
            r = search(root.right, val)
            return r or l
        
        res = search(root, val)
        return res