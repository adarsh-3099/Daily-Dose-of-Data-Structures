'''
Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32      
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50      
Output:  7 and 40
-> Key is to start at end of an array
-> Take l = 0 and r = n-1 (assume ar1 has length m and ar2 has length n) and take diff = sys.maxsize
-> While ( l<m and r>=0)
	If abs(ar1[l] + ar2[r] - x) > diff:
		diff =  abs(ar1[l] + ar2[r] - x)
	(Move r-=1 if ar1[l]+ar2[r] > x else move l-=1)
'''

def printClosest(ar1, ar2, m, n, x):
   diff = sys.maxsize
   l = 0
   r = n-1
   while (r>=0 and l<m):
       if abs(ar1[l]+ar2[r]-x) < diff:
           diff = abs(ar1[l]+ar2[r]-x)
      
       if ar1[l]+ar2[r] > x:
           r -= 1
       else:
           l += 1
   return diff
