class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        low = 0
        high = n-1
        
        while low<=high:
            mid = (low+high)//2
            
            if(mid>0 and mid<n-1):
                
                if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                    return mid
                
                elif(nums[mid]>nums[mid-1]):
                    low = mid+1
                    
                else:
                    high = mid-1
                    
            elif(mid == 0):
                if(nums[mid]>nums[mid+1]):
                    return 0
                else:
                    return 1
            
            else:
                if(nums[mid]>nums[mid-1]):
                    return n-1
                else:
                    return n-2