class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        
        def comb(idx,A,res,ds,remain):
            if idx == len(A):
                return
            
            if remain < 0:
                return
            
            if remain == 0:
                res.append(ds.copy())
                
            else:
                ds.append(A[idx])
                comb(idx,A,res,ds,remain-A[idx])
                ds.pop()
                comb(idx+1,A,res,ds,remain)
            
            
        if not A:
            return 
        
        A = list(set(A))
        res = []
        ds = []
        comb(0,A,res,ds,B)
        res.sort()
        return res