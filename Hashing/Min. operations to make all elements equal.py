'''
-> result is len(arr) - (highest freq. element)
'''

def func(arr):
   d = {}
   for i in arr:
       if i in d:
           d[i] += 1
       else:
           d[i] = 1
   return len(arr) - max(d.values())
