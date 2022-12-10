def sumOfSubarrayOfSizeK(arr, k, target):
   i = 0
   j = 0
   s = 0
   res = []
   while j<len(arr):
       if j-i < k:
           s += arr[j]
           j += 1
       else:
           if s == target:
               return True
           s -= arr[i]
           i += 1
   if s == target:
       return True
   return False
  
 
 
print(sumOfSubarrayOfSizeK([1, -2, 3, -4, 5, 6], 2, 111))
  
