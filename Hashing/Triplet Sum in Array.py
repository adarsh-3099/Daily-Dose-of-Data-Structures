'''->Run loop in from i -> 0-n
->take a set and make curr_sum = sum-A[i] so we just need to find a pair with sum as curr_sum and again run a loop from i+1-n.
->see if curr_sum-A[j] in set. If yes return true
->add A[j] to set.
'''

def find3Numbers(A, arr_size, sum):
   for i in range(0, arr_size-1):
       # Find pair in subarray A[i + 1..n-1]
       # with sum equal to sum - A[i]
       s = set()
       curr_sum = sum - A[i]
       for j in range(i + 1, arr_size):
           if (curr_sum - A[j]) in s:
               print("Triplet is", A[i],
                       ", ", A[j], ", ", curr_sum-A[j])
               return True
           s.add(A[j])
   
   return False
