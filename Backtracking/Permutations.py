class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
        def perm(A,ds,res,freq):
            if len(ds)==len(A):
                res.append(ds.copy())
                return
            
            for i in range(len(A)):
                if not freq[i]:
                    freq[i] = True
                    ds.append(A[i])
                    perm(A,ds,res,freq)
                    ds.pop()
                    freq[i] = False
                    
        if not A:
            return []
            
        freq = [False for i in range(len(A))]
        res = []
        ds = []
        perm(A,ds,res,freq)
        return res