'''  
-> Take l = 0 and r = n-1
If for any l and r such that A[l]+A[r]<x then all pairs b/w l - r has sum < x
Increment l+=1 to chck for other pairs.
Otherwise r+=1
'''

class Solution:
    def pairsSumLessThanX(self, nums: List[int], x) -> List[int]:
        i = 0
        j = len(nums)-1
        res = 0
        while l<x:
            if A[l]+A[r] < x:
               res += (r-l)
		       l += 1
            else:
                r -= 1
        return res
