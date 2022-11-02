'''  
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.
-> Find middle element and break the node.
-> Reverse the next half.
-> Two pointers to find max. sum pair.
'''

class Solution:
   def pairSum(self, head: Optional[ListNode]) -> int:
      
       def rev(head):
           p = head
           q = None
           r = None
           while p:
               r = q
               q = p
               p = p.next
               q.next = r
           head = q
           return head
      
       p = head
       c = 0
       while p:
           c += 1
           p = p.next
          
       mid = c//2
       q = head
       for i in range(mid-1):
           q = q.next
          
       tail = q.next
       q.next = None
       temp_tail = rev(tail)
      
       p = head
       q = temp_tail
       res = -1*2**31
       while p and q:
           x = p.val if p else 0
           y = q.val if q else 0
           res = max(res, x+y)
           p = p.next
           q = q.next
       return res
