'''  
-> Make even integers 0 and odd as 1 and then question is converted to count subarray with k sum
'''

class Solution:
   def numberOfSubarrays(self, nums: List[int], k: int) -> int:
       nums = [i%2 for i in nums]
       d = dict()
       d[0] = 1
       count = sums = 0
       for i in nums:
           sums += i
           count += d.get(sums-k, 0)
           d[sums] = d.get(sums, 0)+1
          
       return count
