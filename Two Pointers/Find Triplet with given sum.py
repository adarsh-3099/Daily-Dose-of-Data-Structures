'''  
-> Sort the array.
Take l = i+1 and r = n-1 and then use two pointer
'''

class Solution:
   #Function to find triplets with zero sum.   
   def findTriplets(self, arr, n):
        arr.sort()
        for i in range(n-1):
            l = i+1
            r = n-1
            while l<r:
                t = arr[i]+arr[l]+arr[r]
                if t == target:
                    return [i,l,r]
                elif t > 0:
                    r -= 1
                else:
                    l += 1
        return [-1,-1,-1]
