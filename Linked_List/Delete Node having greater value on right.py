'''  
Input:
LinkedList = 12->15->10->11->5->6->2->3
Output: 15 11 6 3
Explanation: Since, 12, 10, 5 and 2 are
the elements which have greater elements
on the following nodes. So, after deleting
them, the linked list would like be 15,
11, 6, 3.

-> Reverse LL and take maxi = -1
-> Loop through LL and delete element is smaller than maxi
-> Otherwise update maxi
-> Reverse the LL again and return head
'''

class Solution:
   def compute(self,head):
       #Your code here
       if not head:
           return
      
       def rev(head):
           p = head
           q = None
           r = None
           while p:
               r= q
               q = p
               p = p.next
               q.next = r
           head = q
           return head
          
       h1 = rev(head)
       p = h1
       maxi = -1
       q = None
       while p:
           if maxi > p.data:
               q.next = p.next
               p.next = None
               p = q.next
           else:
               maxi = p.data
               q = p
               p = p.next
              
      
       res = rev(h1)
       return res
