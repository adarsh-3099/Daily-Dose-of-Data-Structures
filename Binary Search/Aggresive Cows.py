class Solution:
    def solve(self,n,k,stalls):
        
        def isValid(stalls, dist, k):
            cows = 1
            lastPos = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - lastPos >= dist:
                    cows += 1
                    lastPos = stalls[i]
                    if cows >= k:
                        return True
            return False
        
        stalls.sort()
        low = 1
        high = stalls[-1] - stalls[0]
        res = 0
        while low <= high:
            mid = (low + high)//2
            if isValid(stalls, mid, k):
                res = mid 
                low = mid + 1
            else:
                high = mid-1
                
        return res