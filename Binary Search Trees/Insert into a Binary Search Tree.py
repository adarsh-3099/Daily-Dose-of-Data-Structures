class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        def InsertHelper(root,data):
            if root is None:
                node = TreeNode(data)
                return node
            
            if data < root.val:
                root.left = InsertHelper(root.left,data)
                return root
            
            else:
                root.right = InsertHelper(root.right,data)
                return root
            
        return InsertHelper(root,val)