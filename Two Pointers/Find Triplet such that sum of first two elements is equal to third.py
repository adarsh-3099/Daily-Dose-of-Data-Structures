'''  
-> Sort the array 
-> Take i = n-1 
while (i>=0):
	l = 0
	r = i-1
	Now chck using two pointer if for any l and r is arr[l]+arr[r] == arr[i]
	i -= 1
'''

class Solution:
   #Function to find triplets with zero sum.   
   def findTriplets(self, arr, n):
       arr.sort()
       i = n-1
       while i>=0:
           l = 0
           r = i-1
           while l<r:
               t = arr[l] + arr[r]
               if t == arr[i]:
                   return True
               elif t > arr[i]:
                   r -= 1
               else:
                   l += 1
           i -= 1
       return False
