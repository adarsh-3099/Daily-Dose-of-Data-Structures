class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i = 0
        j = len(nums)-1
        res = -1
        while i<=j:
            m = i + (j-i)//2
            print(m)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                res = m
                j = m-1
            else:
                i = m+1
                
        if res == -1:
            return len(nums)
        
        return res