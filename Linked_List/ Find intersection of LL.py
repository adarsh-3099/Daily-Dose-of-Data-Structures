def findIntersection(head1,head2):
   #return head
   seen = Counter()
   p = head1
   while p:
       seen[p.data] += 1
       p = p.next
  
   q = head2
   dummy = Node(0)
   curr = dummy
  
   while q:
       if q.data in seen:
           curr.next = Node(q.data)
           curr = curr.next
           seen[q.data] -= 1
           if seen[q.data] == 0:
               seen.pop(q.data)
       q = q.next
   #print(curr)
   return dummy.next
