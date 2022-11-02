def removeDuplicates(head):
   #code here
   if not head:
       return None
      
   if not head.next:
       return head
      
   p = head.next
   q = head
   while p:
       if p.data == q.data:
           q.next = p.next
           p.next = None
           p = q.next
       else:
           q = q.next
           p = p.next
   return head

