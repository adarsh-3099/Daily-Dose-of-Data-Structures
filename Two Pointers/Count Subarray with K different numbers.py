'''  
ans = atMostK(s, k) - atMostK(s, k-1)
'''

class Solution:
   def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
      
       def atMost(arr,k):
           look = collections.Counter()
           i = j = 0
           res = 0
           count = 0
          
           while j<len(arr):
               look[arr[j]] += 1
               if look[arr[j]] == 1:
                   count += 1
               j += 1
               while i<j and count>k:
                   look[arr[i]] -= 1
                   if look[arr[i]] == 0:
                       count -= 1
                   i += 1
               res += j-i
              
           return res
      
       return atMost(nums,k) - atMost(nums,k-1)  