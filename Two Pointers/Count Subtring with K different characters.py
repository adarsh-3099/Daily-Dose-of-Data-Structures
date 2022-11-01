'''
ans = atMostK(s, k) - atMostK(s, k-1)
'''

class Solution:
   def substrCount (self,s, k):
       # your code here
       def atMost(arr,k):
           look = Counter()
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
       a = atMost(s, k)
       b = atMost(s, k-1)
       #print(a, b)
       return a-b
