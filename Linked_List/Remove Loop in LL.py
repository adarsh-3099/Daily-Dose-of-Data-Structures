def isCircular(head):
   # Code here
   if not head and not head.next:
       return 0
  
   slow = head
   fast = head.next
   while(slow and fast and fast.next):
       if slow == fast:
           return 1
       slow = slow.next
       fast = fast.next.next
   return 0