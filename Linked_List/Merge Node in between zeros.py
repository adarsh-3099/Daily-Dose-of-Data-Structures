'''
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
'''

class Solution:
   def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
       dummy = ListNode(0)
       curr = dummy
      
       p = head.next
       while p:
           num = 0
           while p and p.val != 0:
               num += p.val
               p = p.next
           curr.next = ListNode(num)
           curr = curr.next
           p = p.next
       return dummy.next
