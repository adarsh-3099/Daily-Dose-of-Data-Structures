# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    
        
        def T(r, l):
            if r is None:
                return []
            T(r.left, l)
            l.append(r.val)
            T(r.right, l)
            return l
        
        l1 = T(root1, [])
        l2 = T(root2, [])
        #print(l1,l2)
        li = []
        
        i = j = 0
        
        if l1 == []:
            return l2
    
        if l2 == []:
            return l1
    
        if l1 == [] and l2 == []:
            return []
        
        while (i<len(l1) and j<len(l2)):
            if l1[i] < l2[j]:
                li.append(l1[i])
                i += 1
            elif l2[j] < l1[i]:
                li.append(l2[j])
                j += 1
            else:
                li.append(l1[i])
                li.append(l2[j])
                i += 1
                j += 1
        
        if i<len(l1):
            while i<len(l1):
                li.append(l1[i])
                i += 1
                
        if j<len(l2):
            while j<len(l2):
                li.append(l2[j])
                j += 1
        
        return li