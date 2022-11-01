'''
-> take sums = 0 and loop through array
-> at every iteration add element to sums
If k != 0 then make sums = sums%k
If sums is there in dict return True if i-d[sums] > 1 as we want a subarray with length 2 or more
else make d[sums] = i

Example:
nums = [23,2,4], k = 6
Lets walk through the code with the example. 
(i=0) : sums = 23 => 23%6 => (sums = 5)
(i=1) : sums = 5+2=7 => 7%6 => (sums = 1)
(i=2) : sums = 1+4=5 => 5%6 => (sums = 5)
We have encountered the same sums(remainder) again which means we have the subarray of sums%k = 0.
But, there's another aspect to this problem. The subarray must have a minimum size of 2.
That is why we check if (i - d[sums])>1.
In the above example, this if loop is executed when (i=2) and (d[sums]=1).
In other words, the same remainder(sums=5) has been encountered twice and then we check for the respective difference in indices.
Counter example to understand this. Lets take nums = [23,6], k = 6
(i=0) : sums = 23 => 23%6 => (sums = 5)
(i=1) : sums = 5+6=11 => 11%6 => (sums = 5)
'''

class Solution:
   def checkSubarraySum(self, nums: List[int], k: int) -> bool:
       curr = 0
       d = {0: -1}
       for i in range(len(nums)):
           curr += nums[i]
           if k != 0:
               curr = curr%k
           if curr in d:
               if i-d[curr] > 1:
                   return True
           else:
               d[curr] = i
       return False
