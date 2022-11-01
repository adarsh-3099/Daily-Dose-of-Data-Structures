# Iterative
class Solution:
  
   #Function to count nodes of a linked list.
   def getCount(self, head_node):
       #code here
       c = 0
       p = head_node
       while p:
           c += 1
           p = p.next
       return c

# Recursive
class Solution:
  
   #Function to count nodes of a linked list.
   def getCount(self, head_node):
       #code here
       def func(head):
           if head == None:
               return 0
           return 1 + func(head.next)
          
       c = func(head_node)
       return c
