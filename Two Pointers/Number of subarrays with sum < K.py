'''  
-> Take two pointer start = 0 and end = 0 and third var sum = 0
-> while (start < n and end < n):
	If sum < K:
		End += 1 (increment end)
		If (end >= start):
			Count += end - start  (as all the sub arrays between end and start will have sum < K)

		If (end < n):
			Sum += A[end] 
	elif sum > K:
		Sums -= A[start]  //remove elements from start
		start += 1  //increment start
'''

def countSubarrays(arr, n, k):
 
   start = 0
   end = 0
   count = 0
   sum = arr[0]
 
   while (start < n and end < n) :
       if (sum < k) :
           end += 1
 
           if (end >= start):
               count += end - start
 
           if (end < n):
               sum += arr[end]
              
       else :
           sum -= arr[start]
           start += 1
 
   return count
