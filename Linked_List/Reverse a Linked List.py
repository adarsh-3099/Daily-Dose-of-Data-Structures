class Solution:
   #Function to reverse a linked list.
   def reverseList(self, head):
       # Code here
       p = head
       q = r = None
       while p:
           r = q
           q = p
           p = p.next
           q.next = r
          
       head = q
       return head
