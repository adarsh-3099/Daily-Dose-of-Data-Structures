class Solution:
   def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
       c = 0
       p = head
       while p:
           c += 1
           p = p.next
          
       mid = c//2
      
       if mid == 0:
           return None
      
       p = head
       q = None
       for i in range(mid):
           q = p
           p = p.next
      
       q.next = p.next
       del p
       p = q.next
      
       return head
