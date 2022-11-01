''' 
-> Find loop using Floyd Cycle detection method.
-> Take slow as head and fast as it’s posn.
-> Move slow and fast by one point and where they meet is starting point of loop.
'''

class Solution:
   #Function to check if the linked list has a loop.
   def detectLoop(self, head):
       #code here
       if not head or not head.next:
           return False
          
       slow = head
       fast = head.next
      
       while fast and fast.next:
           if slow == fast:
               break
           slow = slow.next
           fast = fast.next.next
      
       slow = head
       while (slow != fast):
           if slow == fast:
               return slow
           slow = slow.next
           fast = fast.next
	   return -1
