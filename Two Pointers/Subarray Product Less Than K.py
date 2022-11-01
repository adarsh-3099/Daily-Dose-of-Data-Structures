'''  
-> Take two pointers start = 0 and end = 0
while end<n:
	-> multiply A[end] to s
	-> while s>k remove elements from start
	-> count += end-start+1
'''

class Solution:
   def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
      
       start = end = 0
       count = 0
       n = len(nums)
       s = 1
       while end<n:
           s = s*nums[end]
           if s >= k:
               while s>=k and start<=end:
                   s = s//nums[start]
                   start += 1
           count += end - start + 1
           end += 1
       return count

