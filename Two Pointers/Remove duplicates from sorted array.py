'''  
-> Take two pointers i = 0 and j = 0
-> Loop through array and if arr[i] == arr[i-1] then i+=1 and decrease n-=1
-> else arr[i] = arr[j] and i+=1 and j+=1 it’ll remove all the duplicate elements.
TC - (O(N))
'''

class Solution:
   def removeDuplicates(self, nums: List[int]) -> int:
       n=len(nums)
       li=[]
       j=0
       i=0
       while(i<len(nums)):
           f=-1
           if i>0 and nums[i]==nums[i-1]:
               n-=1
               i+=1
               continue
              
           nums[j]=nums[i]
           j+=1
           i+=1 
       return n
