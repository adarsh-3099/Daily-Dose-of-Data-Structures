# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        
        result = ""

        def pre_order(node: TreeNode, result):
            if node is None:
                return result
            result += str(node.val) + " "
            if node.left:
                result = pre_order(node.left, result)
            if node.right:
                result = pre_order(node.right, result)
            return result

        ans =  pre_order(root, result)
        print(ans)
        return ans

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        
        temp = data.split()
        
        if not temp:
            return None
        
        root = TreeNode(int(temp[0]))
        
        def bst(root,val):
            if val<root.val:
                if root.left:
                    bst(root.left,val)
                else:
                    root.left = TreeNode(val)
            
            if val>root.val:
                if root.right:
                    bst(root.right,val)
                else:
                    root.right = TreeNode(val)
            return 
        
        for i in temp:
            bst(root,int(i))
        return root

