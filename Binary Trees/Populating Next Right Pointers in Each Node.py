class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return
        
        q = [root]
        nq = []
        
        while q:
            t = None
            for r in q:
                r.next = t
                t = r
                if r.right:
                    nq.append(r.right)
                if r.left:
                    nq.append(r.left)
            q = nq
            nq = []
        
        return root