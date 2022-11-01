'''  
-> Take p=head and q=head.next.
-> count number of nodes is count is odd reduce it by to make it even as we want to swap pairs so we should have even numbers.
-> run a loop till i<count and increment i+=2 every time.
-> swap p and q and move both by two pointers.
'''

class Solution:
   def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if not head:
           return
      
       if head and not head.next:
           return head
      
       c = 0
       p = head
       while p:
           c += 1
           p = p.next
      
       if c%2 == 1:
           c -= 1
      
       p = head
       q = head.next
       i = 0
       while i<c:
           p.val, q.val = q.val, p.val
           p = p.next.next if p.next else None
           q = q.next.next if q.next else None
           i += 2
       return head
