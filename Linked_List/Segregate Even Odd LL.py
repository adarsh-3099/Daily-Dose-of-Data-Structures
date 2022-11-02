'''  
Input: 
N = 7
Link List:
17 -> 15 -> 8 -> 9 -> 2 -> 4 -> 6 -> NULL

Output: 8 2 4 6 17 15 9

Explaination: 8,2,4,6 are the even numbers 
so they appear first and 17,15,9 are odd 
numbers that appear later.
'''

class Solution:
   def divide(self, N, head):
       # code here
       evn = Node(0)
       odd = Node(0)
       evnHead = even
       oddHead = odd
      
       while head:
           if head.data % 2 == 0:
               evn.next = head
               evn = evn.next
           else:
               odd.next = head
               odd = odd.next
           head = head.next
          
       ev.next = oddHead.next
       odd.next = None
       return evnHead.next
