class Solution:
   def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
       def build(ino, post):
           if not post:
               return
 
           rootData = post[-1]
           root = TreeNode(rootData)
           rootIdx = -1
           for i in range(len(ino)):
               if ino[i] == rootData:
                   rootIdx = i
                   break
 
           if rootIdx == -1:
               return
 
           leftIno = ino[:rootIdx]
           rightIno = ino[rootIdx+1:]
 
           lenLeftTree = len(leftIno)
 
           leftPost = post[:lenLeftTree]
           rightPost = post[lenLeftTree:len(post)-1]
 
           root.left = build(leftIno, leftPost)
           root.right = build(rightIno, rightPost)
 
           return root
      
       root = build(inorder, postorder)
       return root
