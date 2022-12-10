def sumOfAllSubarrayOfSizeK(arr, k):
   i = 0
   j = 0
   s = 0
   res = []
   while j<len(arr):
       if j-i < k:
           s += arr[j]
           j += 1
       else:
           res.append(s)
           s -= arr[i]
           i += 1
   res.append(s)
   print(res)
 
 
sumOfAllSubarrayOfSizeK([1, -2, 3, -4, 5, 6], 2)
