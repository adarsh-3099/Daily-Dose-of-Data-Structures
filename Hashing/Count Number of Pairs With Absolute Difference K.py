class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        d = {}    
        c = 0
        for i in nums:
            c += d.get(i-k, 0) + d.get(i+k, 0)
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        return c
