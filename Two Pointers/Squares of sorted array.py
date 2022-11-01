class Solution:
   def sortedSquares(self, nums: List[int]) -> List[int]:
       i = 0
       j = len(nums)-1
       li = []
       for x in range(len(nums)):
           if abs(nums[i]) > abs(nums[j]):
               li.append(nums[i]**2)
               i += 1
           else:
               li.append(nums[j]**2)
               j -= 1
       return li[::-1]
