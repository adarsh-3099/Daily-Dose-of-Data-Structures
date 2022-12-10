class Solution:
    def maximumSumSubarray (self,k,arr,N):
        # code here 
        i = s = 0
        res = -1*2**31
        for i in range(k):
            s += arr[i]
            
        res = max(res, s)
        
        for i in range(k, N):
            s = s - arr[i-k] + arr[i]
            res = max(res, s)
            
        return res
