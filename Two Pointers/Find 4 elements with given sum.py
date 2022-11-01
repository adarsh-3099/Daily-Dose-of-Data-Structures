'''  
-> Sort the array.
	for ( i -> 0 <-> n3):
		for ( j -> i+1 <-> n-2)
			Use two pointer to find arr[l] and arr[r] such that
			arr[l] + arr[r] + arr[i] + arr[j] == target
	TC - (O(N**3))
'''

def find4Numbers(A, n, X):
   A.sort()
 
   for i in range(n - 3):
       for j in range(i + 1, n - 2):
           l = j + 1
           r = n - 1
 
           while (l < r):
               if(A[i] + A[j] + A[l] + A[r] == X):
                   return [i, j, l, r]
                   l += 1
                   r -= 1
              
               elif (A[i] + A[j] + A[l] + A[r] < X):
                   l += 1
               else:
                   r -= 1
   return [-1, -1, -1, -1]
