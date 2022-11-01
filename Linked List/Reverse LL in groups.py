'''
(BRUTE)
-> Take an empty list and run a loop while we don’t hit None
-> Take an inner loop which find elements in k groups and append to an empty list li which is then pop( ) into res so element of k group is reversed 
-> If the group does not have k size group take it as it is and dont reverse
-> Now res[ ] has the data in required format simply assign the values starting from first node to end.
'''

class Solution:
   def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
      
       if head is None:
           return
      
       p = head
       li = []
       res = []
       while p:
          
           c = 0
           while p and c<k:
               li.append(p.val)
               p = p.next
               c += 1
          
           if c == k:
               while li:
                   res.append(li.pop())
           else:
               while li:
                   #print(li[-1])
                   res.append(li.pop(0))
      
       p = head
       for i in res:
           p.val = i
           p = p.next
      
       return head

''' OPTIMIZED '''

class Solution:
   def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
      
       if head is None or k == 1:
           return head
      
       dummy = ListNode(0)
       dummy.next = head
       curr = dummy
       pre = dummy
       nex = dummy
      
       cnt = 0
       p = head
       while p:
           cnt += 1
           p = p.next
      
       while cnt >= k:
           curr = pre.next
           nex = curr.next
          
           for i in range(1, k):
               curr.next = nex.next
               nex.next = pre.next
               pre.next = nex
               nex = curr.next
              
           pre = curr
           cnt -= k
  
       return dummy.next
