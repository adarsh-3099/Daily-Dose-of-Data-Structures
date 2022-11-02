class Solution:
   def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
      
       seen = set()
       p = headA
       while p:
           seen.add(p)
           p = p.next
          
       q = headB
       while q:
           if q in seen:
               return q
           q = q.next
      
       return None
