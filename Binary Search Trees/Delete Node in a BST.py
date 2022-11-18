class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        def deleteRoot(root):
            if not root.right:
                return root.left
            left = root.left
            root =  root.right
            node = root
            while node.left:
                node = node.left
            node.left = left
            return root
        
        if not root: return
        if root.val == key: return deleteRoot(root)
        node,parent = root,root
        flg_left,flg_right = 0,0      # these two flags denote whether the node if the left subtree or right subtree of the parent
        while node.val != key and (node.left or node.right):
            parent = node
            if node.val > key and node.left:
                node = node.left
                flg_left,flg_right = 1,0
            elif node.val < key and node.right:
                node = node.right
                flg_left,flg_right = 0,1
        if node.val == key and flg_left:
            parent.left = deleteRoot(node)
        elif node.val == key and flg_right:
            parent.right = deleteRoot(node)
        return root