class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True
        
        start, end = 2, num
        while start<=end:
            mid = start + (end-start)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                start = mid+1
            else:
                end = mid-1
                
        return False