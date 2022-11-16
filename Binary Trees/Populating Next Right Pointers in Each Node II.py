"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        q = [root]
        nq = []
        
        while q:
            prev = None
            for r in q:
                r.next = prev
                prev = r
                if r.right:
                    nq.append(r.right)
                if r.left:
                    nq.append(r.left)
            q = nq
            nq = []
        return root        