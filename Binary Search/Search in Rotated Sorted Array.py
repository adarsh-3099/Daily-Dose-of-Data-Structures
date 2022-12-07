class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def BS(arr,s,e,t):
            while s<=e:
                m = s+(e-s)//2
                if arr[m] == t:
                    return m
                elif arr[m] > t:
                    e = m-1
                else:
                    s = m+1
            return -1
        
        
        start = 0
        idx = -1
        end = len(nums)-1
            
        if len(nums) == 1:
            idx = 0
        
        elif nums[0] <= nums[-1]:
            idx = 0
        
        else:
            while start<=end:
                mid = start+(end-start)//2
                
                if nums[mid] > nums[mid+1]:
                    idx = mid+1
                    break
                
                if nums[mid-1] > nums[mid]:
                    idx = mid
                    break
                    
                if nums[mid] > nums[start]:
                    start = mid+1
                
                else:
                    end = mid-1
                
        r1 = BS(nums,0,idx,target)
        r2 = BS(nums,idx,len(nums)-1,target)
        
        return max(r1,r2)
            