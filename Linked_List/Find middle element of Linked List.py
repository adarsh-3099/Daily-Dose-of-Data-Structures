class Solution:
   def findMid(self, head):
       # Code here
       # return the value stored in the middle node
       if not head:
           return
       slow = head
       fast = head
       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
       return slow.data
