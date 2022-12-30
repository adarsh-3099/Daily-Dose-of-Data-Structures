class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        
        def subset(idx,res,ds,A):
            if idx == len(A):
                res.append(ds.copy())
                return
            
            subset(idx+1,res,ds+[A[idx]],A)
            subset(idx+1,res,ds,A)
            
            
        res = []
        ds = []
        A.sort()
        subset(0,res,ds,A)
        r = sorted(res)
        return r