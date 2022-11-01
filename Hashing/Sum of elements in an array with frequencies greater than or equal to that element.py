def func(arr, k):
   d = {}
   for i in range(len(arr)):
       if arr[i] in d:
           d[arr[i]] += 1
       else:
           d[arr[i]] = 1
  
   s = 0
   for i in d.keys():
       if d[i] >= i:
           s += i
   return s
