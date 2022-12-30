""" A backtracking approach to get all subsets """


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        
        def sub(A,res,ds,idx,N):
            if idx == N:
                res.append(ds)
                return
            
            sub(A,res,ds+[A[idx]],idx+1,N)
            sub(A,res,ds,idx+1,N)
                
        res = []
        ds = []
        A.sort()
        sub(A,res,ds,0,len(A))
        r = sorted(res)
        return r