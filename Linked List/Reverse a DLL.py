'''  
-> Traverse DLL using a pointer and swap prev and next pointer of each element
-> At last change head of DLL
'''

def reverseDLL(head):
   #return head after reversing
   while head:
       t = head.next
       head.next = head.prev
       head.prev = t
       if head.prev == None:
           break
      
       head = head.prev  # as we make prev to next so we have to move to prev to go to next element
   return head
