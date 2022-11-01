def func(arr, k):
   d = {}
   for i in range(len(arr)):
        if arr[i] in d:
            if abs(i - d[arr[i]]) == k:
               return True
            d[arr[i]] = i
        else:
           d[arr[i]] = i
   return False
