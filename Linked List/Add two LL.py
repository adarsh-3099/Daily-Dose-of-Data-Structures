'''Reverse both LL and then find sum then reverse the resultant linked list.'''

class Solution:
   #Function to add two numbers represented by linked list.
   def addTwoLists(self, first, second):
       # code here
       # return head of sum list
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
          
       l1 = rev(first)
       l2 = rev(second)
       dummy = Node(0)
       curr = dummy
       c = 0
       while l1 and l2:
           v1 = l1.data if l1 else 0
           v2 = l2.data if l2 else 0
          
           d = v1 + v2 + c
           c = d//10
           d = d%10
          
           curr.next = Node(d)
           curr = curr.next
          
           l1 = l1.next if l1 else None
           l2 = l2.next if l2 else None
          
       while l1:
           d = l1.data + c
           c = d//10
           d = d%10
           curr.next = Node(d)
           curr = curr.next
           l1 = l1.next
      
       while l2:
           d = l2.data + c
           c = d//10
           d = d%10
           curr.next = Node(d)
           curr = curr.next
           l2 = l2.next
      
       if c > 0:
           curr.next = Node(c)
      
       res = rev(dummy.next)
       return res
