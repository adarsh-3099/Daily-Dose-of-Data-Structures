'''  
-> Reverse LL
-> Add 1 starting from front.
-> Reverse and return LL
'''

class Solution:
   def addOne(self,head):
       #Returns new head of linked List.
      
       temp=head
       arr=[]
       while temp!=None:
           arr.append(temp.data)
           temp=temp.next
       n=0
       for i in arr:
           n=n*10+i
       n=n+1
       res = [int(x) for x in str(n)]
       ll1=LinkedList()
       for i in res:
           ll1.insert(i)
      
       return ll1.head
