'''  
https://leetcode.com/problems/reverse-linked-list-ii/
'''

class Solution:
   def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
      
       if not head:
           return None
      
       p=head
       s=head
      
       for i in range(left-1):
           p=p.next
          
       li = []
       q = p
       for j in range(left-1,right):
           li.append(q.val)
           q=q.next
          
          
       print(li)
       li = li[::-1]
       for i in li:
           p.val = i
           p = p.next
          
       return head
