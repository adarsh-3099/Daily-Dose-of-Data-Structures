'''  
-> Take odd = head and even = head.next and eHead = even
-> Run loop till even and even.next does not exist
-> Attach the next element after next element to odd and even so that we can get odd and even index elements together
'''

class Solution:
   def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
       if not head or not head.next:
           return head
      
       odd = head
       even = head.next
       eHead = even
      
       while even and even.next:
           odd.next = odd.next.next
           even.next = even.next.next
          
           odd = odd.next
           even = even.next
          
          
       odd.next = eHead
       return head
class Solution:
   def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
       if not head or not head.next:
           return head
      
       odd = head
       even = head.next
       eHead = even
      
       while even and even.next:
           odd.next = odd.next.next
           even.next = even.next.next
          
           odd = odd.next
           even = even.next
          
          
       odd.next = eHead
       return head
class Solution:
   def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
       if not head or not head.next:
           return head
      
       odd = head
       even = head.next
       eHead = even
      
       while even and even.next:
           odd.next = odd.next.next
           even.next = even.next.next
          
           odd = odd.next
           even = even.next
          
          
       odd.next = eHead
       return head
