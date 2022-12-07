class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        def isValid(A,N,K,mid):
            student = 1
            s = 0
            for i in range(N):
                s += A[i]
                if s>mid:
                    student += 1
                    s = A[i]
                
                if student > K:
                    return False
            return True
            
        
        start = max(A)
        end = sum(A)
        res = -1
        while start <= end:
            mid = start + (end-start)//2
            
            if isValid(A,N,M,mid):
                res = mid
                end = mid-1
                
            else:
                start = mid+1
        return res