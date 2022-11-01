def removeDuplicates(head):
   seen = set()
   p = head
   while p:
       if p in seen:
           return True
       seen.add(p)
   return False


'''
-> Two Pointers
Take slow = fast = head
Run a loop till fast and fast.next exists (as fast will move by two points)
Check if at any instance slow == fast then return True and at each step move slow = slow.next and fast = fast.next.next
'''

def detectLoop(self, head):
       #code here
       if not head or not head.next:
           return False
        
       slow = head
       fast = head.next
      
       while fast and fast.next:
           if slow == fast:
               return True
           slow = slow.next
           fast = fast.next.next
      
       return False
