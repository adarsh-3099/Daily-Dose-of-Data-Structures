class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        i = 1
        n = len(arr)
        
        while i<n-1:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                return i
            i += 1
        return -1
        
            