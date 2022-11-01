'''
-> Sort the array
-> Take l = i+1 and r = n-1
	Then use pointer to find triplets with zero sum
'''

class Solution:
   #Function to find triplets with zero sum.   
   def findTriplets(self, arr, n):
       arr.sort()
       for i in range(n):
           l = i+1
           r = n-1
           while l<r:
               t = arr[i]+arr[l]+arr[r]
               if t == 0:
                   return 1
               elif t > 0:
                   r -= 1
               else:
                   l += 1
       return 0
 
