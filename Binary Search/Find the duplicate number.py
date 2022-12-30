class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        m = {}
        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
                
                
        for i in m.keys():
            if m[i] > 1:
                return i