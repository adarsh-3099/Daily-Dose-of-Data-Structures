class Solution:
	# @param A : integer
	# @param B : integer
	# @return a list of list of integers
	def combine(self, A, B):
        def func(res, ds, vis, nums):
            if len(ds) == len(nums):
                if len(ds) == B:
                    res.append(ds.copy())
                return
            
            for i in range(len(nums)):
                if not vis[i]:
                    vis[i] = True
                    ds.append(nums[i])
                    func(res, ds, vis, nums)
                    ds.pop()
                    vis[i] = False
                
            return res
        
        nums = [i+1 for i in range(A)]
        vis = [False for i in range(len(nums))]
        res = func([], [], vis, nums)
        return res