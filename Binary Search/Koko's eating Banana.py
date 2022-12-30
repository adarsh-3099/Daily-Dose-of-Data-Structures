class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles) == 1 and h>piles[0]:
            return 1
        
        def isValid(arr,h,mid):
            r = 0
            for i in range(len(arr)):
                x = arr[i]
                temp = x//mid
                if x%mid > 0:
                    temp += 1
                r += temp
                if r>h:
                    return False
            return True
        
        start = 1
        end = max(piles)
        res = -1
        while start<=end:
            mid = (end+start)//2
            print(mid)
            if (isValid(piles,h,mid)):
                res = mid
                end = mid-1
            else:
                start = mid+1
            
        return res