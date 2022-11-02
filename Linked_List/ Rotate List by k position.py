'''  
-> find count of elements in LL (let’s say c)
-> if c==0 or k is multiple of c just return head as no need to rotate
-> else find c-k posn element (let’s say p and q is element just befor p) and take a pointer to last element (let’s say r)
r.next = head
q.next = None
head = p
'''

class Solution:
   def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      
       if not head or not head.next:
           return head
      
       c = 0
       p = head
       while p:
           c += 1
           p = p.next
      
       if c == 0 or k % c == 0:
           return head
      
       if k > c:
           k = k%c
      
       posn = c-k
       p = head
       q = None
       for i in range(posn):
           q = p
           p = p.next
      
       r = head
       while r.next:
           r = r.next
          
       r.next = head
       q.next = None
       head = p
       return head
