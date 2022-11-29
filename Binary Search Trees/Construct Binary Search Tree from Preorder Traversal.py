# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        ino = preorder[::]
        ino.sort()
        
        def buildTrees(preorder,inorder):
            if len(preorder)==0:
                return None
        
            rootData = preorder[0]
            root = TreeNode(rootData)
        
            rootIdx=-1
            for i in range(0,len(inorder)):
                if rootData==inorder[i]:
                    rootIdx=i
                    break
                
            leftInOrder=inorder[0:rootIdx]
            rightInOrder=inorder[rootIdx+1:]
        
            leftSubTree=len(leftInOrder)
        
            leftPreOrder=preorder[1:leftSubTree+1]
            rightPreOrder=preorder[leftSubTree+1:]
        
            leftChild=buildTrees(leftPreOrder,leftInOrder)
            rightChild=buildTrees(rightPreOrder,rightInOrder)
        
            root.left=leftChild
            root.right=rightChild
        
            return root
        
        x=buildTrees(preorder,ino)
        return x