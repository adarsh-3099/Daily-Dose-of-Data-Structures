class Solution:
   #Function to remove duplicates from unsorted linked list.
   def removeDuplicates(self, head):
       # code here
       # return head after editing list
       if not head or not head.next:
           return head
      
       seen = set()
       q = head
      
       while q.next:
           seen.add(q.data)
           if q.next.data in seen:
               q.next = q.next.next
           else:
               q = q.next
        
       return head
