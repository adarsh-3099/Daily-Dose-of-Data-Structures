''' 
Optimal - -> Make a freq dict.
Loop through array and replace i from target
If i == target-i: cnt += d[target-i]-1 as we want to omit extra occurance
else: cnt += d[target-i]
'''

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:   
        ans=0
        cnt = Counter(nums)
        for i in nums:
            x = target.replace(i, "", 1) 
            #print(x)
            if x in cnt:
                if x == i:
                    ans += cnt[x] - 1
                else:
                    if i+x == target:
                        ans += cnt[x]
        return ans
