'''  
-> Take p and q move p to last and q to 2nd last
-> p.next = head then head = p
-> q.next = None. This is how me move last element to first
'''

class Solution:
   #Function to remove a loop in the linked list.
   def moveLastToFirst(self, head):
       if not head or head.next:
           return head
 
       p = head
       q = None
       while p.next:
           q = p
           p = p.next
 
       p.next = head
       q.next = None
       head = p
       return head