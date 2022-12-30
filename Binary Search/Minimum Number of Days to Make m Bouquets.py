""" Another variation of min-pages """

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m*k > len(bloomDay):
            return -1
        
        if m*k == len(bloomDay):
            return max(bloomDay)
        
        
        if len(bloomDay) == 1 and h>bloomDay[0]:
            return 1
        
        def feasible(days) -> bool:
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m
        
        start = 1
        end = max(bloomDay)
        res = -1
        while start<=end:
            mid = (end+start)//2
            #print(mid)
            if feasible(mid):
                res = mid
                end = mid-1
            else:
                start = mid+1
            
        return res