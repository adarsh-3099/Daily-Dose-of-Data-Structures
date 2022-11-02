def getNthFromLast(head,n):
   #code here
   c = 0
   p = head
   while p:
       c += 1
       p = p.next
   if c-n < 0:
       return -1
   p = head
   for i in range(c-n):
       p = p.next
   return p.data

