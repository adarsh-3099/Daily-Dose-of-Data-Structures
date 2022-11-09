class Solution:
   def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
      
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
      
       root=buildTrees(preorder,inorder)
       return root
