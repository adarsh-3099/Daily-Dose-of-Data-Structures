'''  
Input: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 , P = 2
Output: 3 <-> 4 <-> 5 <-> 6 <-> 1 <-> 2
Explanation: Doubly linked list after rotating
2 nodes is: 3 4 5 6 1 2.

-> Make it a circular linked list by last.next = head and head.prev = last
-> Move head by p points. Let node before p posn in nthNode
-> Break the link of head.
head = nthNode.next
nthNode.next = None
head.prev = None
'''

class Solution():
   def rotateDLL(self, start, p):
       if not start:
           Return
      
       c = 0
       q = start
       while q:
           c += 1
           q = q.next
      
       if c == 0 or p%c == 0:
           return head
      
       if p>c:
           p = p%c
          
       last = start
       while last.next:
           last = last.next
          
       last.next = start
       start.prev = last
      
       nthNode = start
       for i in range(p-1):
           nthNode = nthNode.next
          
       start = nthNode.next
       start.prev = None
       nthNode.next = None
       return start


